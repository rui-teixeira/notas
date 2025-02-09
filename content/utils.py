# grade_utils.py

import numpy as np

def generate_dummy_grades(num_exams: int, num_questions: int, seed: int = None) -> list:
    """
    Generate a dummy dataset of exam grades.

    Each exam is represented as a list of binary values, where 1 indicates a correct answer 
    and 0 indicates an incorrect answer.

    Parameters:
        num_exams (int): The number of exams to generate.
        num_questions (int): The number of questions per exam.
        seed (int, optional): A random seed for reproducibility. Defaults to None.

    Returns:
        list: A list of lists, where each inner list represents an exam's scores.
    """
    if seed is not None:
        np.random.seed(seed)
    grades = np.random.randint(0, 2, (num_exams, num_questions)).tolist()
    return grades

def sum_columns(matrix):
    """
    Sums the values of each column in a list of lists (matrix).

    Parameters:
        matrix (list of list of int): The matrix to sum columns from.

    Returns:
        list of int: A list containing the sum of each column.
    """
    return [sum(col) for col in zip(*matrix)]