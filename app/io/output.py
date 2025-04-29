def print_text_to_console(text):
    """
    Prints the given text to the console.

    Args:
        text (str): The text to print.
    """
    print(text)


def write_text_to_file_builtin(filepath, text):
    """
    Writes the given text to a file using Python's built-in functions.

    Args:
        filepath (str): The path to the file.
        text (str): The text to write.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)


def write_text_to_file_with_pandas(filepath, dataframe):
    """
    Writes the given DataFrame to a file using the pandas library.

    Args:
        filepath (str): The path to the output file.
        dataframe (pandas.DataFrame): The DataFrame to write.
    """
    try:
        dataframe.to_csv(filepath, index=False)
    except Exception as e:
        print(f"Error writing file with pandas: {e}")
