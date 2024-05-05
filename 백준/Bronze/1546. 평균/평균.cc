#include<iostream>
using namespace std;

int main() {
    int s;
    int max=0,sum=0,count=0;
    cin>>s;
    int arr[s];
    for(int i=0;i<s;i++)
    {
        cin>>arr[i];
        if(max<arr[i])
            max=arr[i];
        sum+=arr[i];
        count++;
    }
    cout<<(float)sum/(max*count)*100;
}