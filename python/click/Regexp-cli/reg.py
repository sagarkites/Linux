#!/usr/bin/env python 

import click 
import re

@click.command()
@click.option('--f', type=str, help='Give the name of file.')
@click.option('--old', type=str, help='Give Present String.')
@click.option('--new', type=str, help='Give new string for Replacement.')

def cli(f,old,new):    
    with open (f, 'r') as f:
         content = f.read()
         content_new=re.sub(old, new, content)
         print content_new
         
if __name__ == '__main__':
   cli()
