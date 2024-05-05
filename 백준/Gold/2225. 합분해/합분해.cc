#include<iostream>
using namespace std;

#define Moduler 1000000000

int main()
{
    int n, k;
    cin>>n>>k;
    long long int arr[201][201]={0,};
    for(int i=1;i<201;i++)
    {
        arr[0][i]=1;
        arr[i][0]=1;
        arr[i][1]=1;
        arr[i][2]=i+1;
    }
    for(int i=1;i<201;i++)
    {
        for(int j=3;j<201;j++)
        {
            for(int p=0;p<=i;p++)
            {
                arr[i][j]+=arr[p][j-1];
            }
            arr[i][j]=arr[i][j]%Moduler;
        }
    }
    cout<<arr[n][k];
}