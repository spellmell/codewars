
# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

"""
In this kata, you will write a function that returns the positions and the
values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with
a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks.
Both of these properties should be arrays. If there is no peak in the given
array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays
(although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
(in the context of a mathematical function, we don't know what is after and
before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3]
and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the
position and value of the beginning of the plateau. For example:
pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]}
(or equivalent in other languages)

Have fun!
"""

from random import randint as r

min = 500000000
max = 1000000000


def pick_peaks(arr):
    arr, index, value, psi = list(map(int, arr)), [], [], 0

    for i, v in enumerate(arr):
        if 0 < i < len(arr)-1:
            p, n = arr[i-1], arr[i+1]
            if p < v > n:
                [index.append(i), value.append(v)]
            if p != v == n:  # starting plateau
                psi = i  # initial index of plateau
                # print(f"psi:{psi}")
            if p == v > n and v > arr[psi-1] and arr[0] != arr[1]:
                # print(f"psi:{psi}")
                [index.append(psi), value.append(v)]

    print(f"{arr}\npos:{index}\npeaks:{value}")

    return {'pos': index, 'peaks': value}


pick_peaks(list(str(r(min, max))))
# pick_peaks([8, 8, 5, 3, 7, 1, 3, 5, 7, 8, 2, 1, 3])
