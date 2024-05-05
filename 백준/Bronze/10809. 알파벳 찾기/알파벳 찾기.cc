#include<iostream>
#include<string.h>
#include<memory.h>
using namespace std;

int main(){
    string str;
    int arr[26];
    cin>>str;
    int i=str.length();
    memset(arr,-1,sizeof(arr));
    for(int j=0;j<i;j++)
    {
        if(arr[str[j]-'a']==-1)
            arr[str[j]-'a']=j;
    }
    for(int j=0;j<26;j++)
        cout<<arr[j]<<" ";
}