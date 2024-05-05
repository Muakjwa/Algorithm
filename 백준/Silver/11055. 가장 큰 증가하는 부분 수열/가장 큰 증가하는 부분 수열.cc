#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n,result=0;
    cin>>n;
    int arr[1001];
    int dp[1001]={0,};
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        dp[i]=arr[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            if (arr[i]>arr[j])
            {
                dp[i]=max(dp[i],arr[i]+dp[j]);
            }
        }
        result=max(result,dp[i]);
    }
    cout<<result<<'\n';
    return 0;
}