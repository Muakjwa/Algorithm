#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int a=n/2;
    int arr[15];
    arr[0]=3;
    if(n%2==1)
    {
        cout<<0<<endl;
        return 0;
    }
    for(int i=1;i<a;i++)
    {
        arr[i]=3*arr[i-1]+2;
        for(int j=i-2;j>=0;j--)
        {
            arr[i]+=2*arr[j];
        }
    }
    cout<<arr[a-1];
}