#include<iostream>
#include<string>
using namespace std;

int main()
{
    string st;
    while(getline(cin,st))
    {
        int sm=0,ca=0,num=0,blank=0;
        for(int i=0;i<st.length();i++)
        {
            if(st[i]-' '==0)
            {
                blank++;
            }
            else if(st[i]-'a'>=0 && st[i]-'a'<26)
            {
                sm++;
            }
            else if(st[i]-'A'>=0 && st[i]-'A'<26)
            {
                ca++;
            }
            else if(st[i]-'0'>=0 && st[i]-'0'<10)
            {
                num++;
            }
        }
        cout<<sm<<' '<<ca<<' '<<num<<' '<<blank<<'\n';
    }
    return 0;
}