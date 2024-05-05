#include<iostream>
using namespace std;

int main(){
    int s;
    cin>>s;
    for(int i=0;i<s;i++)
    {
        int a;
        int sum=0,count=0;
        cin>>a;
        int arr[a];
        for (int j=0;j<a;j++)
        {
            cin>>arr[j];
            sum+=arr[j];
        }
        sum=sum/a;
        for(int j=0;j<a;j++)
        {
            if(arr[j]>sum)
                count+=1;
        }
        cout<<(float)count*100/a<<"%"<<endl;
    }
}