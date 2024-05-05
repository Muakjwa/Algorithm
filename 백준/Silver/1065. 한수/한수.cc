#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    if (n<100)
        cout<<n;
    else
    {
        int count=99;
        for(int i=100;i<n+1;i++)
        {
            int h=i/100;
            int t=(i%100)/10;
            int o=i%10;
            if(h-t==t-o)
                count+=1;
        }
        cout<<count;
    }
}