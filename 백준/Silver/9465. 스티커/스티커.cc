#include<iostream>
#include<algorithm>
using namespace std;


int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        int arr[100001][2];
        for(int j=0;j<x;j++)
        {
            int k;
            cin>>k;
            arr[j][0]=k;
        }
        for(int j=0;j<x;j++)
        {
            int k;
            cin>>k;
            arr[j][1]=k;
        }
        arr[1][0]+=arr[0][1];
        arr[1][1]+=arr[0][0];
        
        for(int j=2;j<x;j++)
        {
            arr[j][0]=arr[j][0]+max(arr[j-1][1],arr[j-2][1]);
            arr[j][1]=arr[j][1]+max(arr[j-1][0],arr[j-2][0]);
        }
        
        cout<<max(arr[x-1][0],arr[x-1][1])<<'\n';
    }
}