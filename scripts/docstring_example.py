def add_one(x: int | float) -> int | float:
    """Add a one to an input variable and return the output

    Args:
        x (int | float): the input

    Returns:
        int | float: the input with one added
    """
    return x + 1

def add_one_int(x: int) -> int:
    """Add a one to an input variable and return the output

    Args:
        x (int): the input

    Returns:
        int: the input with one added
    """
    assert isinstance(x, int)
    return x + 1