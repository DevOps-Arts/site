import os, sys

try:
    f = open("con.txt", "r")
    f = f.read()
    print(f)
    os.chdir("cons")
    print("runing! under construction")
    os.system("python3 -m http.server 8005")
except:
    print(" construction == 'false'")
    os.system("python3 -m http.server 8005")
