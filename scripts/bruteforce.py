import subprocess

string = "bruteforce"
test = "4 0 0 0 0 0"
t = [4, 0, 0, 0, 0, 0]

def execute(cmd, args):
    popen = subprocess.Popen(cmd, args, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

while t[5] > 9:
        output = subprocess.Popen(["./bomb", "result"])
        output.stdout.close()
        # output = execute("./bomb", ["result"])
        t[1] += 1
        if t[1] > 9:
                t[1] = 0
                t[2] += 1
        if t[2] > 9:
                t[2] = 0
                t[3] += 1
        if t[3] > 9:
                t[3] = 0
                t[4] += 1
        if t[4] > 9:
                t[4] = 0
                t[5] += 1

        test = str(t[0]) + " " + str(t[1]) + " " + str(t[2]) + " " + str(t[3]) + " " + str(t[4]) + " " + str(t[5])
        print(test)
        # print("==========================================================")
        # print(output.communicate())
        # print("==========================================================")
        string = test

