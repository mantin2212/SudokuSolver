from copy import copy


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
