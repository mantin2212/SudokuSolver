from copy import copy
import numpy as np


def copy_matrix(mat):
    """
    Clone two-dimensional list (matrix).
    :param list(list) mat: The matrix to clone.
    :return: A clone of the matrix
    :rtype: list(list)
    """
    return [copy(line) for line in mat]


def is_unique(lst):
    """
    Check if list elements are unique.
    :param list lst: The list to check.
    :return: True if the list's elements are unique, and false otherwise.
    :rtype: bool
    """
    return len(set(lst)) == len(lst)


def to_list(matrix):
    """
    Convert matrix to list.
    :param list matrix: The matrix to convert.
    :return: A list containing the matrix values.
    :rtype: list
    """
    length = len(matrix) * len(matrix[0])
    return np.reshape(matrix, length).tolist()


def repr_raw_list(lst):
    result = ""
    for e in lst:
        result += "{} ".format(e)
    result = result[:-1]
    return result
