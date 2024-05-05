#include<iostream>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int array[10000];
    for(int i=0;i<n;i++)
    {
        cin>>array[i];
    }
    for(int i=0;i<n;i++)
    {
        if(array[i]<m)
        {
            cout<<array[i]<<" ";
        }
    }
}