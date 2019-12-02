# Aws-boto script 
import boto3
import paramiko
ec2 = boto3.resource('ec2') 
vol = ec2.Volume('vol-id')
# Detach-volume --> (Volume & Instance_Ids)  
res = vol.detach_from_instance(Device='/dev/xvda', Force=True|False, InstanceId='id')
print res
# Attach-volume --> (Instance_Id & Device_name)
attach = vol.attach_to_instance(Device='/dev/xvde', InstanceId='id')
print attach
# Authintication to Ec2 Ianstance and Mount Ebs
k = paramiko.RSAKey.from_private_key_file("/home/vagrant/.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect( hostname = "Dns",username = "user",pkey = k )
commands = [ "sudo mkdir -p /mnt/scott","sudo mount -t xfs -o nouuid /dev/xvde1 /mnt/scott" ]
for command in commands:
        print "Executing {}".format( command )
        stdin , stdout, stderr = c.exec_command(command)
        print stdout.read()
        print( "Errors")
        print stderr.read()
c.close()
