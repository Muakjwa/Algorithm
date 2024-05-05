#include<iostream>
using namespace std;

int func(int i){
    int sum=0;
    sum+=i;
    while(i!=0){
        sum=sum+i%10;
        i/=10;
    }
    if(sum>10000){
        return 0;
    }
    return sum;
}

int main(){
    int array[10001]={0};
    for(int i=0;i<10000;i++){
        array[func(i)]=1;
    }
    for(int i=0;i<10001;i++){
        if(array[i]==0){
            cout<<i<<"\n";
        }
    }
    return 0;
}