from pathlib import Path
from typing import List


def verify(parameter: str, name: str) -> None:
    """
    Verify if parameter is blank, if so, raise ValueError.
    """
    if not parameter or parameter == '""' or parameter == '" "':
        raise ValueError(f"{name} cannot be blank!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot begin or end with an empty space!")


def read_from(file: Path) -> str:
    with open(file, mode = "r") as f_obj:
        for line in f_obj:
            yield line.strip()


def write_to_file(file_name: Path, items: List[str]) -> None:
    with open(file_name, "a") as f_obj:
        for item in items:
            f_obj.write(f"{item}\n")


def main():

    try:

        partial_txt_file_path = input("File Path: ").strip()
        verify(parameter = partial_txt_file_path, name = "File Path")
        
        complete_txt_file_path = Path.home().joinpath(partial_txt_file_path)
        validate_file_type(file_name = complete_txt_file_path)

        output = Path(complete_txt_file_path.parent).joinpath("output").with_suffix(".txt")

        itemized : List[str] = []

        for line in read_from(file = complete_txt_file_path):
            if line.endswith("."):
                print(f"\item {line}")
                itemized.append(f"\item {line}")
            else:
                print(f"\item {line}.")
                itemized.append(f"\item {line}.")
        
        write_to_file(file_name = output, items = itemized)
    
    except (FileNotFoundError, ValueError) as e:
        print(e)
        
if __name__ == '__main__':
    main()
