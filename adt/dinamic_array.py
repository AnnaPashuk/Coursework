import ctypes
import sys
print(sys.path)


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._array_a = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._array_a[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._array_a[self._n] = obj
        self._n += 1

    def _resize(self, size_capacity):  # nonpublic utitity
        """Resize internal array to capacity size_capacity."""
        array_b = self._make_array(size_capacity)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            array_b[k] = self._array_a[k]
        self._array_a = array_b  # use the bigger array
        self._capacity = size_capacity

    def _make_array(self, size_capacity):  # nonpublic utitity
        """Return new array with capacity size_capacity."""
        return (size_capacity * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._array_a[j] = self._array_a[j - 1]
        self._array_a[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._array_a[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._array_a[j] = self._array_a[j + 1]
                self._array_a[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item

                return  # exit immediately
        raise ValueError("value not found")  # only reached if no match
