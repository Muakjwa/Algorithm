#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[100001],dp[100001]={0,};
    cin>>arr[0];
    dp[0]=arr[0];
    int mx=dp[0];
    for(int i=1;i<n;i++)
    {
        cin>>arr[i];
        if (dp[i-1]>0)
        {
            dp[i]=arr[i]+dp[i-1];
        }
        else{
            dp[i]=arr[i];
        }
        mx=max(mx,dp[i]);
    }
    cout<<mx;
}