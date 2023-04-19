from difflib import Differ


def find_diff(text1, text2):
    diff = Differ()
    difference = list(
        diff.compare(text1.decode("utf-8").splitlines(keepends=True), text2.decode("utf-8").splitlines(keepends=True)))

    # Coloring the output
    for i, line in enumerate(difference):
        if line.startswith('+'):
            difference[i] = "\033[32m" + line + "\033[0m"
        elif line.startswith('-'):
            difference[i] = "\033[31m" + line + "\033[0m"
        elif line.startswith('?'):
            difference[i] = "\033[34m" + line + "\033[0m"
        else:
            difference[i] = "\033[0m" + line + "\033[0m"

    return ''.join(difference)
