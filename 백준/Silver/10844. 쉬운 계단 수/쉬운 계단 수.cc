#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int sum=0;
    long long arr[101][10]={{0,1,1,1,1,1,1,1,1,1}};
    for(int i=1;i<n;i++)
    {
        arr[i][0]=arr[i-1][1];
        arr[i][9]=arr[i-1][8];
        for(int j=1;j<9;j++){
            arr[i][j]=(arr[i-1][j-1]+arr[i-1][j+1])%1000000000;
        }
    }
    for(int i=0;i<10;i++)
    {
        sum=(sum+arr[n-1][i])%1000000000;
    }
    cout<<sum;
    return 0;
}