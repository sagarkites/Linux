# Shell script basic keywords
* **#!bin/bash** - it tells the interpreter that the following lines are written for bash known as shebang
* **echo** - used to display line of text/string
* **read** - Reads the data until you press the enter key
    * **read -p** - prompts to enter something 
    * **read -n** - limits the number of letter entering
    * **read -s** - prompts for the secure string generally used for password
* **sh** - is the bourne shell and command interpreter that takes your input, provides output back to the screen
    * **sh -nv** -checks the synax of the specfic shell script before executig, -n --noexec, -v --versbose mode 
    * **sh -x** - starts debugs the every line of script before executing 
    * **sh +x** - ends debugs the every line of script before executing 
    * **set -** - starts debugs in script
    * **set +** - ends debugs in scripts
     * **set -e** - check if any errors in the scripts and stops the entire script execution  
