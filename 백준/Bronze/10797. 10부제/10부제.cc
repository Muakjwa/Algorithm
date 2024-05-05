#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int cnt=0,i;
    while(!(cin>>i).eof()){
        if(n==i){
            cnt+=1;
        }
    }
    cout<<cnt;
    return 0;
}