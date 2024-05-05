#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n,mx=0;
    cin>>n;
    int arr[1001],dp[2][1001];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        dp[0][i]=1;
        dp[1][i]=1;
        for(int j=0;j<i;j++)
        {
            if(arr[i]>arr[j])
            {
                dp[0][i]=max(dp[0][i],dp[0][j]+1);
            }
        }
    }
    for(int i=n-1;i>=0;i--)
    {
        for(int j=n-1;j>i;j--)
        {
            if(arr[j]<arr[i])
            {
                dp[1][i]=max(dp[1][i],dp[1][j]+1);
            }
        }
        mx=max(mx,dp[0][i]+dp[1][i]);
    }
    cout<<mx-1;
}