#include<iostream>
using namespace std;

int main(){
    int a,b;
    int b_1,b_2,b_3,result;
    cin>>a;
    cin>>b;
    result=a*b;
    b_1=b/100;
    b_2=(b%100)/10;
    b_3=b%10;
    cout<<a*b_3<<endl;
    cout<<a*b_2<<endl;
    cout<<a*b_1<<endl;
    cout<<result<<endl;
}