#include<iostream>
using namespace std;
 
int main()
{
    int n;
    cin>>n;
    int arr[1001];
    arr[1]=1;
    arr[2]=3;
    for(int i=3;i<n+1;i++)
    {
        arr[i]=(2*arr[i-2]+arr[i-1])%10007;
    }
    cout<<arr[n];
    return 0;
}