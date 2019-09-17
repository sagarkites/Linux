# Syntax Diffrences b/w Python and Shell
# veriables
| Python | shell |
| --- | --- |
|a=0|a=1|
|print(a)|echo $a|
# expressions
| Python | shell |
| --- | --- |
|a + b|`expr a + b`|
|a - b|`expr a - b`|
|a * b|`expr a * b`|
|a % b|`expr a % b`|
# Data-stucures
| Python | shell |
| --- | --- |
|list|array|
|dic|
|set|
|tuple|
# Loops
| Python | shell |
| --- | --- |
|for i range(10),print(i)| for i in (( i=1; i<=10; i++ ));do echo $i; done|
|x= [i for i in range(10) if i % 2 == 0],print(x)|i=1,until [ $i -gt 100 ];do echo $i; done|
|i=1,while i<10:,print(i),i+=1|i=1,while [ $i -le 100 ];then echo $i; done|
# Conditions
| Python | shell |
| --- | --- |
|if a <10:| if [ $a -le 10 ];then echo $a; fi |
