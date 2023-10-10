#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return numpy multiplication of mat.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
