#!/bin/bash
# capture the signals in the script and write own logic
trap "rm -rf /home/vagrant/scott.txt; exit" 2
for i in {1..100}
do
   sleep 4
   echo $i
done
