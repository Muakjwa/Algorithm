#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int arr[1001]={0,1,2,};
    for(int i=3;i<n+1;i++)
    {
        arr[i]=(arr[i-1]+arr[i-2])%10007;
    }
    cout<<arr[n];
}