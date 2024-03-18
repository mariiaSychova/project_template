import pandas as pd


def output_text_to_console(*args, **kwargs):
    """Prints text to the console.

    Example:
        >>> output_text_to_console("Hello, world!")
        Hello, world!

    Args:
        *args: Positional arguments representing the text to be printed.
        **kwargs: Keyword arguments for optional formatting options supported by the print function.

    Returns:
        None
    """
    print(*args, **kwargs)


def write_to_file_using_built_in_python_capabilities():
    """Writes content to a file using built-in Python capabilities.

    Returns:
        None
    """
    with open('./data/content_written_using_built_in_python_capabilities.txt', 'w') as file:
        file.write("These words will be written to the file.")


def write_to_file_using_pandas():
    """Writes content to a file using pandas library.

    Returns:
        None
    """
    content = pd.read_csv('./data/test.csv')
    content.to_csv('./data/content_written_using_pandas.csv')
