#!/usr/bin/python
from sshconf import read_ssh_config, empty_ssh_config
from os.path import expanduser


# User prompts
i = input(str('enter host -->'))
j = input(str('enter hostname -->'))
k = input(str('enter user -->'))
l = input(str('enter port -->'))

# Creates config file
c = empty_ssh_config()
c.add(i, Hostname=j, User=j, Port=l,)
# writes to path
c.write("/Users/pavanscott/.ssh/config")
#Prints the resposnse
print(i, c.host(i))
#adds to same file attributes 
c.add("host_1", Hostname="scott", User="ubuntu", Port=22)
c.write("/Users/pavanscott/.ssh/config")
# remove 
#c.remove("host_1")

# Adds to EOL
f = open('/Users/pavanscott/.ssh/config', 'a')
f.write("IdentityFile =/nfs/shared/users/nixcraft/keys/server1/id_rsa")
f.close()
