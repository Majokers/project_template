from app.io.input import read_text_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import print_text_to_console, write_text_to_file_builtin

def main():

    console_text = read_text_from_console()
    file_text = read_file_builtin('input.txt')
    pandas_text = read_file_with_pandas('data.csv')


    print_text_to_console(console_text)
    print_text_to_console(file_text)
    print_text_to_console(pandas_text)


    write_text_to_file_builtin('output_console.txt', console_text)
    write_text_to_file_builtin('output_file_builtin.txt', file_text)
    write_text_to_file_builtin('output_pandas.txt', pandas_text)


if __name__ == '__main__':
    main()
