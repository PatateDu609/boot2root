from hashlib import sha256
import os

files = os.listdir("./ft_fun/")
files = [f for f in files if f.endswith(".pcap")]
dest = [] # list of files in order to be written in the destination file
dfile = "./ft_fun.c"

for file in files:
    content = open("./ft_fun/" + file, "r").read()
    comment = content.find("//")
    nb = int(content[comment + 6:])

    entry = {"id": nb, "filename": file}
    dest.append(entry)

dest = sorted(dest, key=lambda k: k['id'])

dfile = open(dfile, "w")
for d in dest:
    content = open("./ft_fun/" + d["filename"], "r").read()
    dfile.write(content + "\n")

os.system("gcc ft_fun.c")
os.system("./a.out > ft_fun.txt")

ft_fun = open("./ft_fun.txt", "r").read()

print(ft_fun)

password = ft_fun.split("\n")[-2]
password = password.split(" ")[-1]

print("Hashed password: " + sha256(password.encode()).hexdigest())