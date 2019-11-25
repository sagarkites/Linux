#!/usr/bin/python
import json
import argparse

def inv():
    data = {
      "servers": {
           "hosts": ['host-name', 'host-name'],
           "vars": {
               "ansible_ssh_user": "user"
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
