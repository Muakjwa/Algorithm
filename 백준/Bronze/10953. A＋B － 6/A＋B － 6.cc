#include<iostream>
#include<string>
using namespace std;

int main()
{
    int n;
    cin>>n;
    string s="";
    for (int i=0;i<n;i++)
    {
        int a,b;
       
        cin>>s;
        a=s[0]-'0';
        b=s[2]-'0';
        cout<<a+b<<endl;
    }
}