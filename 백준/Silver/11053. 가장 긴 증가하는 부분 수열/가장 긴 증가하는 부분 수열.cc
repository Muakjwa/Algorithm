#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n,mx=0;
    cin>>n;
    int arr[1001],dp[1001];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        int idx=0;
        for(int j=0;j<i;j++)
        {
            if (arr[j]<arr[i])
            {
                idx=max(idx,dp[j]);
            }
        }
        dp[i]=idx+1;
        mx=max(mx,dp[i]);
    }
    cout<<mx;
}