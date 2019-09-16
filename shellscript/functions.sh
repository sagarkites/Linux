#!/bin/bash
# use source to execute function in runtime (source .sh; fun)
fun() {
     for i in {1..100}
     do
        echo $i
     done   
}     
