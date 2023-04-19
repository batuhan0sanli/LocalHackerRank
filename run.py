import subprocess

from src import colorize

file_name = "main.py"
inputs = open("problem_details/input.txt", "r").read().encode("utf-8")
expected_output = open("problem_details/output.txt", "r").read().encode("utf-8")

cmd = [
    'python',
    file_name
]

process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = process.communicate(inputs)

if err:
    print(colorize("Runtime Error :(", "red"))
    print(colorize("\n----- Error Output (stderr) -----", "blue"))
    print(colorize(err.decode("utf-8"), "red"))
    exit(0)

out = out[:-1]
if out == expected_output:
    print(colorize("Congratulations!", "green"))


else:
    # find out & expected_output differences
    print(
        colorize("Wrong Answer :(\n", "red"),
        colorize("\n----- Your Output (stdout) -----\n", "blue"),
        colorize(out.decode("utf-8"), "yellow"),
        colorize("\n----- Expected Output -----\n", "blue"),
        colorize(expected_output.decode("utf-8"), "green")
    )
