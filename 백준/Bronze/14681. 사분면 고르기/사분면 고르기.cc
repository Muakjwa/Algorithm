#include<iostream>
using namespace std;

int main(){
    int a,b;
    cin>>a;
    cin>>b;
    if(a*b>0)
    {
        if(a>0)
            cout<<1;
        else
            cout<<3;
    }
    else
    {
        if(a>0)
            cout<<4;
        else
            cout<<2;
    }
}