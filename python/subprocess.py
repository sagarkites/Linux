import subprocess
i=subprocess.call("ls -altr", shell=True) # Gives output with exit status shell=True says /bin/sh -c
j=subprocess.check_call(["mkdir", "sagar"]) #Gives the output without exit status
print i
if j == 0: 
   subprocess.call('touch /home/vagrant/sagar/scott.txt', shell=True)
   
