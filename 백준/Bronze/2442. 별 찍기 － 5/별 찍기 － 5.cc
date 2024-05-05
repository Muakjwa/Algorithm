#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=1;i<n+1;i++){
        for(int j=n;j>i;j--){
            cout<<" ";
        }
        for(int j=0;j<i*2-1;j++){
            cout<<"*";
        }
        cout<<"\n";
    }
    return 0;
}