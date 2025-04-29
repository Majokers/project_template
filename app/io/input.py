import pandas as pd

def read_text_from_console():
    """
    Reads text input from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")


def read_file_builtin(filepath):
    """
    Reads text from a file using Python's built-in functions.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."


def read_file_with_pandas(filepath):
    """
    Reads data from a file using the pandas library.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The content of the file as a string (without index).
    """
    try:
        df = pd.read_csv(filepath)
        return df.to_string(index=False)
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except pd.errors.EmptyDataError:
        return f"Error: File '{filepath}' is empty."
