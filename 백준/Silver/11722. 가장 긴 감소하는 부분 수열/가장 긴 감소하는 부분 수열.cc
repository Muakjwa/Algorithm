#include<iostream>
using namespace std;

int main()
{
    int n,mx=0;
    cin>>n;
    int arr[1001],dp[1001];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        dp[i]=1;
        for(int j=0;j<i;j++)
        {
            if(arr[i]<arr[j])
            {
                dp[i]=max(dp[i],dp[j]+1);
            }
        }
        mx=max(mx,dp[i]);
    }
    cout<<mx;
}