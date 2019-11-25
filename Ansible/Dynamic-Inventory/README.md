# Ansible dynamic inventory
# chmod 755 ec2.py 
# ./ec2.py --list 
# ansible -i ec2.py us-east-1c -u username -m ping
# ansible-playbool name.yml -i ec2.py -u user 
# ansible-playbool name.yml -i ec2.py -u user --limit $instance-ip
