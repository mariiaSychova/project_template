from app.io.input import input_text_from_console, read_from_file_using_built_in_python_capabilities, read_from_file_using_pandas
from app.io.output import output_text_to_console, write_to_file_using_built_in_python_capabilities, write_to_file_using_pandas


def main():
    user_input = input_text_from_console()
    print(user_input)

    file_content = read_from_file_using_built_in_python_capabilities()

    file_content_pandas = read_from_file_using_pandas()

    with open('./data/output.txt', 'w') as file:
        file.write(user_input)
        file.write(file_content)
        file.write(str(file_content_pandas))

    output_text_to_console("Hello!!!")
    write_to_file_using_built_in_python_capabilities()
    write_to_file_using_pandas()


if __name__ == "__main__":
    main()
