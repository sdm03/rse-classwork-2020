def energy(density, coeff=1.0):
    import numpy as np
    """
    Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
    # Force density to be an array
    density = np.array(density)

    # Check values are positive
    if density.dtype.kind != 'i' and len(density) >0:
        raise TypeError("Density is an array of integers")

    # Check values are integers
    if any(density < 0):
        raise ValueError("Density array should only contain positive values")

    # Check array is 1D
    if density.ndim != 1:
        raise ValueError("Density should be a 1D array")

    energy = np.sum( density * (density-1))
    return energy