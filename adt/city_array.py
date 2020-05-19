"""
ADT for hotels app
"""
import ctypes


class CityArray:
    """
    A dynamic array class for saving information
    about hotels and cities.
    """

    def __init__(self):
        """
        Create an empty array.
        """
        self._n = 0
        self._capacity = 1
        self._array_a = self._make_array(self._capacity)

    def __len__(self):
        """
        Return number of elements stored in the array.
        """
        return self._n

    def __getitem__(self, item):
        """
        Return element at index k.
        """
        if not 0 <= item < self._n:
            raise IndexError('invalid index')
        return self._array_a[item]

    def append(self, obj):
        """
        Add object to end of the array.
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array_a[self._n] = obj
        self._n += 1

    def _resize(self, size_capacity):
        """
        Resize internal array to capacity size_capacity.
        """
        array_b = self._make_array(size_capacity)
        for k in range(self._n):
            array_b[k] = self._array_a[k]
        self._array_a = array_b
        self._capacity = size_capacity

    def _make_array(self, size_capacity):
        """
        Return new array with capacity size_capacity.
        """
        return (size_capacity * ctypes.py_object)()

    def size(self):
        """
        Return a size of the array
        """
        return self._capacity
