#include<iostream>
#include<string>
using namespace std;

int main()
{
    int arr[26]={0,};
    string st;
    cin>>st;
    for(int i=0;i<st.length();i++)
    {
        arr[st[i]-'a']++;
    }
    for(int i=0;i<26;i++)
    {
        cout<<arr[i]<<' ';
    }
}