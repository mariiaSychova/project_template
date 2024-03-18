import pandas as pd


def input_text_from_console():
    """Prompts the user to enter text from the console and returns the entered text.

    Returns:
        str: The text entered by the user in the console.
    """
    entered_text = input("Enter your text: ")
    return entered_text


def read_from_file_using_built_in_python_capabilities():
    """Reads the contents of a file using Python's built-in capabilities.

    Returns:
        str: The content of the file as a string.
    """
    with open('./data/test.csv') as file:
        file_content = file.read()
        print(file_content)
        return file_content


def read_from_file_using_pandas():
    """Reads the contents of a file using the Pandas library.

    Returns:
        pandas.DataFrame: The content of the file as a Pandas DataFrame.
    """
    file_content_pandas = pd.read_csv('./data/test.csv')
    print(file_content_pandas)
    return file_content_pandas
