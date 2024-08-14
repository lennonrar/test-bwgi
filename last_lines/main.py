from idlelib.iomenu import encoding

from module import last_lines


def main() -> None:
    for line in last_lines("my_file.txt", buffer_size=1024):
        print(line, end="")


if __name__ == "__main__":
    main()
