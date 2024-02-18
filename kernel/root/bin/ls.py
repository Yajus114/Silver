# to be plugged into the Terminal class
# ls - list directory contents
# syntax: ls [directory] - list the contents of the specified directory


def main(self: object, args: list[str]):
    paths = []
    flags = []
    print(args)
    for arg in args:
        if arg.startswith("-"):
            if len(arg) == 1:
                flags.append(arg)
            else:
                for flag in arg[1:]:
                    flags.append(f"-{flag}")
        else:
            paths.append(arg)
    print(*flags)
    long = "-l" in flags

    if "--h" in flags:
        self.cout("///USAGE///\nls <directory_path> <-a> <-l>\nechoes contents of the directory specified.")
        return
    elif not paths:
        try:
            files = self.list_directory(self.current_directory, long)
        except ValueError as e:
            self.cout(f"///ERROR///\n{e}")
            return
    else:
        try:
            files = self.list_directory(paths[0])
        except ValueError as e:
            self.cout(f"///ERROR///\n{e}")
            return

    for spam, file in enumerate(files):
        if file == "__pycache__":
            files.pop(spam)

    if "-a" not in args:
        if long:
            for i, spam in enumerate(files):
                if spam[-1][0] == ".":
                    files.pop(i)
        for i, eggs in enumerate(files):
            if eggs[0] == ".":
                files.pop(i)
    if not files:
        self.cout("///DIRECTORY EMPTY///")
        return 0

    if long:
        self.tabulate(files)
        return

    self.cout("\n".join(files))
