#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b;
    cin>>a>>b;
    long long int* arr= new long long int[a];
    for(int i=0;i<a;i++)
    {
        cin>>arr[i];
    }
    sort(arr,arr+a);
    cout<<arr[b-1];
}