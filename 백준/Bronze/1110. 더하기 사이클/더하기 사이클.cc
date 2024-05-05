#include<iostream>
using namespace std;

int main()
{
    int n,temp,count=1;
    cin>>n;
    if(n<10)
    {
        n*=10;
    }
    temp=n;
    n=(((n/10)+(n%10))%10)+(n%10)*10;
    while(n!=temp)
    {
        n=(((n/10)+(n%10))%10)+(n%10)*10;
        count++;
    }
    cout<<count;
}