#include<iostream>
using namespace std;

int d(int i){
    int result=0;
    while(i!=0){
        result=result*10+i%10;
        i/=10;
    }
    return result;
}

int main(){
    int a,b;
    cin>>a>>b;
    if(d(a)>d(b)){
        cout<<d(a);
    }
    else{
        cout<<d(b);
    }
    return 0;
}