#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int sum=0;
    for(int i=0;i<5;i++){
        int a;
        cin>>a;
        sum+=pow(a,2);
    }
    cout<<sum%10;
}