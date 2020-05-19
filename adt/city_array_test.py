"""
module for testing city_array ADT
"""
from adt.city_array import CityArray


def func():
    """
    Function for testing city_array
    """

    new_array = CityArray()
    new_array.append(1)
    new_array.append(2)
    new_array.append(3)
    assert new_array.size() == 4
    assert new_array.__getitem__(1) == 2
    assert new_array.__len__() == 3


if __name__ == "__main__":
    try:
        func()
        print("Everything runs correct!")
    except AssertionError:
        print("Something went wrong!")
