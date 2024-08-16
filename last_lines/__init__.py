from main import last_lines


def run() -> None:
    for line in last_lines("data/my_file.txt", buffer_size=1024):
        print(line, end="")


if __name__ == "__main__":
    run()
