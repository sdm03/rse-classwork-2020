from model import energy
from pytest import raises

def test_energy_for_negatives():
    """
    Test function for model.energy()
    """
    with raises(ValueError) as exception: 
        energy([-1, 2, 3])


def test_energy_for_non_integers():
    """
    Test function for model.energy()
    """
    with raises(TypeError) as exception: 
        energy([1.0, 2, 3])


