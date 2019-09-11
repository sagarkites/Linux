# shell script basics
* **#!bin/bash** - it tells the interpreter that the following lines are written for bash known as shebang
* **echo** - used to display line of text/string
* **echo$?** - prints the returns code 
* **read** - Reads the data until you press the enter key
    * **read -p** - prompts to enter something 
    * **read -n** - limits the number of letter entering
    * **read -s** - prompts for the secure string generally used for password
* **sh** - is the bourne shell and command interpreter that takes your input, provides output back to the screen
    * **sh -nv** -checks the synax of the specfic shell script before executig, -n --noexec, -v --versbose mode 
    * **sh -x** - starts debugs the every line of script before executing 
    * **sh +x** - ends debugs the every line of script before executing 
    * **set -options** - starts debugs in script
    * **set +options** - ends debugs in scripts
    * **set -e** - stops script immediately if anything exits with a non-zero status
    * **set -n** - checks the syntax of line and will not execute script 
    * **set -v** - prints everyline and executes the script
* **export** - used to set environment veriables 
* **source** - used to read and execute the content of a file and passed as an argument in the current shell script
    * **source file args** - executes the file
    * **source file; fun** - excutes the functions inside script as a runtime environment 
    
    
    
