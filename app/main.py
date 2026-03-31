def copy_file(command: str) -> None:
    try:
        parts = command.strip().split()
        if len(parts) != 3 or parts[0] != "cp":
            raise ValueError

        _, original_file, new_file = parts
        if original_file == new_file:
            return

        with (open(original_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

    except FileNotFoundError:
        pass
    except ValueError:
        pass
