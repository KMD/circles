#include <Python.h>

int Cfib(int n){
    if(n < 2){
        return n;
    }else{
        return Cfib(n - 1) + Cfib(n - 2);
    }
}