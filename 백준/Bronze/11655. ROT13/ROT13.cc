#include<iostream>
#include<string>
using namespace std;

char small(char c)
{
    if(c>='n')
    {
        c-=13;
    }
    else
    {
        c+=13;
    }
    return c;
}

char big(char c)
{
    if(c>='N')
    {
        c-=13;
    }
    else
    {
        c+=13;
    }
    return c;
}

int main()
{
    string s;
    getline(cin,s);
    for(int i=0;i<s.length();i++)
    {
        if(s[i]>='a' && s[i]<='z')
        {
            s[i]=small(s[i]);
        }
        else if(s[i]>='A' && s[i]<='Z')
        {
            s[i]=big(s[i]);
        }
        cout<<s[i];
    }
}