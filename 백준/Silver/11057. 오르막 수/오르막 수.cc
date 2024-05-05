#include<iostream>
using namespace std;

int main()
{
    int n,result=0;
    cin>>n;
    int arr[1001][10]={{1,1,1,1,1,1,1,1,1,1},{10,9,8,7,6,5,4,3,2,1}};
    for(int i=1;i<n;i++)
    {
        int sum=0;
        for(int j=9;j>=0;j--)
        {
            sum+=arr[i-1][j];
            arr[i][j]=sum%10007;
        }
    }
    for(int i=0;i<10;i++)
    {
        result=(result+arr[n-1][i])%10007;
    }
    cout<<result;
    return 0;
}