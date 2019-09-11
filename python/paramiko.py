import boto3
import paramiko
ec2 = boto3.resource('ec2') 
vol = ec2.Volume('vol-0fc029d73aaabe355')
# Detach-volume --> (Volume & Instance_Ids)  
res = vol.detach_from_instance(Device='/dev/xvda', Force=True|False, InstanceId='i-09a37f61546ea0f9c')
print res
# Attach-volume --> (Instance_Id & Device_name)
attach = vol.attach_to_instance(Device='/dev/xvde', InstanceId='i-048fc703e0baf23c3')
print attach
# Authintication to Ec2 Ianstance and Mount Ebs
k = paramiko.RSAKey.from_private_key_file("/home/vagrant/lambda.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect( hostname = "ec2-18-207-103-233.compute-1.amazonaws.com",username = "ec2-user",pkey = k )
commands = [ "sudo mkdir -p /mnt/scott","sudo mount -t xfs -o nouuid /dev/xvde1 /mnt/scott" ]
for command in commands:
        print "Executing {}".format( command )
        stdin , stdout, stderr = c.exec_command(command)
        print stdout.read()
        print( "Errors")
        print stderr.read()
c.close()
