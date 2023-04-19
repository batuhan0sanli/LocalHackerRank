import subprocess

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
    print("\033[31mError happened when executing your solution:\033[0m")
    print(err.decode("utf-8"))
    exit(0)


out = out[:-1]
if out == expected_output:
    print("\033[32mExpected output\033[0m")

else:
    # find out & expected_output differences
    print("\033[31m!!!!! Unexpected output !!!!!\n\033[0m"
          "\n\033[34m----- Your Output (stout) -----\033[0m\n",
          "\033[31m{}\033[0m\n"
          "\033[34m----- Expected Output -----\033[0m\n"
          "\033[32m{}\033[0m".format(out.decode("utf-8"), expected_output.decode("utf-8")))
exit(0)