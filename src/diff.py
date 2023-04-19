from difflib import Differ
from typing import Optional


class Diff:
    def __init__(self, text1: bytes, text2: bytes):
        self.text1: bytes = text1
        self.text2: bytes = text2
        self.diff_engine: 'Differ' = Differ()
        self.compared: Optional[list] = None

    def compare(self) -> str:
        text1 = self.text1.decode("utf-8").splitlines(keepends=True)
        text2 = self.text2.decode("utf-8").splitlines(keepends=True)
        difference = list(self.diff_engine.compare(text1, text2))

        # Add newline to the end of each line
        difference = [line if line.endswith('\n') else line + '\n' for line in difference]
        # difference = self._get_only_diff(difference)
        return self._colorized_text(difference)

    @staticmethod
    def _get_only_diff(difference) -> list:
        return [line for line in difference if line.startswith('+ ') or line.startswith('- ') or line.startswith('? ')]

    @staticmethod
    def _colorized_text(difference) -> str:

        # Coloring the output
        for i, line in enumerate(difference):
            if line.startswith('+ '):
                difference[i] = "\033[32m" + line + "\033[0m"
            elif line.startswith('- '):
                difference[i] = "\033[31m" + line + "\033[0m"
            elif line.startswith('? '):
                difference[i] = "\033[34m" + line + "\033[0m"
            elif line.startswith('  '):
                difference[i] = "\033[0m" + line + "\033[0m"

        return ''.join(difference)
