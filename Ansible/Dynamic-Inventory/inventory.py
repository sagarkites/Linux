#!/usr/bin/python
import json
import argparse

def inv():
    data = {
      "servers": {
           "hosts": ['ec2-3-82-120-69.compute-1.amazonaws.com', 'ec2-3-87-206-220.compute-1.amazonaws.com'],
           "vars": {
               "ansible_ssh_user": "ec2-user"
            }
       }
    }
    return data

if __name__ == '__main__':
   data = inv()
   p = argparse.ArgumentParser()
   p.add_argument('--list', action='store_true')
   p.add_argument('--host', action='store')
   arg = p.parse_args()
   if arg and arg.list:
      print json.dumps(data)
