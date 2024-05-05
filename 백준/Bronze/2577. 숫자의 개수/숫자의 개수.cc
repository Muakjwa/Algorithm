#include<iostream>
using namespace std;

int main(){
    int a,b,c;
    int array[10]={};
    cin>>a;
    cin>>b;
    cin>>c;
    int x=a*b*c;
    while(x!=0)
    {
        array[x%10]++;
        x/=10;
    }
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<endl;
    }
}