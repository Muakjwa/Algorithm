#include<iostream>
#include<set>
using namespace std;

int main(){
    int arr[10];
    set<int> s;
    for(int i=0;i<10;i++)
    {
        cin>>arr[i];
        arr[i]%=42;
        s.insert(arr[i]);
    }
    cout<<s.size();
}