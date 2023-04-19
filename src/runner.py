import subprocess

from src import colorize, find_diff


class Runner:
    python_command = "python"
    main_file_path = "main.py"
    input_file_path = "problem_details/input.txt"
    output_file_path = "problem_details/output.txt"

    def __init__(self):
        self.inputs = open(self.input_file_path, "r").read().encode("utf-8")
        self.expected_output = open(self.output_file_path, "r").read().encode("utf-8")

        cmd = [
            self.python_command,
            self.main_file_path
        ]
        self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.out, self.err = None, None

    def run(self):
        out, err = self.process.communicate(self.inputs)
        self.out = out[:-1]
        self.err = err
        return self

    def is_correct(self):
        return self.out == self.expected_output

    def print_result(self):
        if self.err:
            print(colorize("Runtime Error :(", "red"))
            print(colorize("\n----- Error Output (stderr) -----", "blue"))
            print(colorize(self.err.decode("utf-8"), "red"))
            exit(0)
        if self.is_correct():
            print(colorize("Congratulations!", "green"))
        else:
            print(
                colorize("Wrong Answer :(", "red") +
                colorize("\n\n----- Differences -----\n", "blue") +
                colorize(find_diff(self.out, self.expected_output), "default") +
                colorize("\n\n----- Your Output (stdout) -----\n", "blue") +
                colorize(self.out.decode("utf-8"), "yellow") +
                colorize("\n\n----- Expected Output -----\n", "blue") +
                colorize(self.expected_output.decode("utf-8"), "green")
            )
