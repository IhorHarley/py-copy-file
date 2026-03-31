def copy_file(command: str) -> None:
    try:
        parts = command.strip().split()
        if len(parts) != 3 or parts[0] != "cp":
            raise ValueError("Invalid command format!")

        _, original_file, new_file = parts
        if original_file == new_file:
            return

        with (open(original_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

    except FileNotFoundError:
        print(f"Error: File {original_file} not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except ValueError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")
