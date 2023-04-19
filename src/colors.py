from enum import Enum


def colorize(text, color):
    color = Colors[color.upper()].value
    return f"{color}{text}{Colors.RESET.value}"


class Colors(Enum):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
