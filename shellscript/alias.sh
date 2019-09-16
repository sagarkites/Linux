#!/bin/bash 

shopt -s expand_aliases
#shopt is the thing that can enable the alias in the scripting 
alias UP="sudo apt-get update"
alias FI="find /home -user dev_ops"
#Here we we use the above veriables as back ticks
A=`UP`
B=`FI`
echo "update the operating system $A"
echo "Find the files in home dir owned by user $B"
