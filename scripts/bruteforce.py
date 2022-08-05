import subprocess, os

t = [4, 0, 0, 0, 0, 0]

while t[5] < 10:
        # p = subprocess.Popen(["./bomb", "result"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        subprocess.run(["./bomb", "result"])
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
        # p.stdin.write(test)
        # p.stdin.close()

