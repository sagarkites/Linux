$1
case $1 in 
     git)
      sudo yum install git -y 
     remove)
      sudo yum remove git -y
     *)
      git --version 
esac      
      
