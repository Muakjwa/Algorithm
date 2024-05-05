#include<iostream>
using namespace std;

int main(){
    int size=0;
    int sum=0;
    cin>>size;
    
    char number[size];
    cin>>number;
    
    for(int i=0;i<size;i++){
        sum+=number[i]-'0';
    }
    cout<<sum;
}