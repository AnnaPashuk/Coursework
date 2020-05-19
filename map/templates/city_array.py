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
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._array_a = self._make_array(self._capacity)  # low-level array

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
        return self._array_a[item]  # retrieve from array

    def append(self, obj):
        """
        Add object to end of the array.
        """
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._array_a[self._n] = obj
        self._n += 1

    def _resize(self, size_capacity):  # nonpublic utitity
        """
        Resize internal array to capacity size_capacity.
        """
        array_b = self._make_array(size_capacity)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            array_b[k] = self._array_a[k]
        self._array_a = array_b  # use the bigger array
        self._capacity = size_capacity

    def _make_array(self, size_capacity):  # nonpublic utitity
        """
        Return new array with capacity size_capacity.
        """
        return (size_capacity * ctypes.py_object)()  # see ctypes documentation

