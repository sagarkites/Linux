#!/usr/bin/env python 
import click
import os 

@click.command()
@click.option('--user', type=str, help='Username of server.')
@click.option('--ip', type=str, help='Ip address of server.')
@click.option('--cmd', type=str, help='Executes the command in server')

def cli(user, ip, cmd):
    i = os.system('ssh -t {}@{} {}'.format(user, ip, cmd))
    print i

if __name__ == '__main__':
   cli() 
