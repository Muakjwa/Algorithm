#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int i=1;
    while(n>i){
        n-=i;
        i++;
    }
    i++;
    if(i%2==1){
        cout<<n<<"/"<<i-n;
    }
    else{
        cout<<i-n<<"/"<<n;
    }
    return 0;
}