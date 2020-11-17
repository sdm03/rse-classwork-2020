import datetime
import requests
from json import loads

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []

    if len(range1) == 0 or len(range2) == 0:
        raise ValueError("Both inputs must have non-zero length")
    
    # Check that start2 is in range 1 and raise exception/ print to console
    for start1, end1 in range1:
        if start1 >  end1:
            raise ValueError("range1 incorrect. Cannot accept backwards time range")
        for start2, end2 in range2:
            if start2 > end2:
                raise ValueError("range2 incorrect. Cannot accept backwards time range")

            if start1 <= end2 and start2 <= end1:
                low = max(start1, start2)
                high = min(end1, end2)
                if high==low:
                    continue
                overlap_time.append((low, high))

    return overlap_time

def iss_passes(latitude, longitude, altitude=None, passes=None):

    base = "http://api.open-notify.org/iss-pass.json?"

    # Ensure they are no bigger than 80 (mag)
    if abs(latitude) > 80 and abs(longitude) > 180:
        raise ValueError("Longitude and latitude must lie within range of -80 to 80")
    else:
        params = {'lat': latitude, 'lon':longitude}
                  
    if altitude is not None and (altitude <= 0 or altitude > 10000):
        raise ValueError("Altitude must lie within range of 0+ to 10000")
    else:
        # Ensure altitude is an integer
        params['alt'] =  altitude
        
    if passes is not None and (passes <= 0 or passes > 100):
        raise ValueError("Number of passes must lie within range of 0 to 100")
    else:
        params['n'] = passes

    response = requests.get(base, params=params).json()['response']
    times = [(str(datetime.datetime.fromtimestamp(i['risetime'])), str(datetime.datetime.fromtimestamp(i['risetime']+i['duration']))) for i in response]
    
    return times


if __name__ == "__main__":
    iss_passes(-20, 50)