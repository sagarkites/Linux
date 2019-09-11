import subprocess

i = subprocess.run("ls", shell=True) # executes with returncode

j = subprocess.run(["ls", "-altr"],capture_output=True)

print(j.stdout.decode()) # prints stdout

print(i)

print(j.stderr.decode()) # prints stderr

k = subprocess.run(["cat","sub.py"], capture_output=True,)

l = subprocess.run(["grep","-n", "k"],capture_output=True, input=k.stdout) # using stdout as stdinput

print(l.stdout.decode())

if j.returncode != 0:
   print("oops! check the code")
