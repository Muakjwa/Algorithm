#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    long long int arr[101];
    arr[1]=1;
    arr[2]=1;
    arr[3]=1;
    arr[4]=2;
    arr[5]=2;
    arr[6]=3;
    for(int i=7;i<101;i++)
    {
        arr[i]=arr[i-1]+arr[i-5];
    }
    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;
        cout<<arr[a]<<endl;
    }
}