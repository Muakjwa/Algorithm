#include<iostream>
using namespace std;

int main(){
    pair<int,int> arr[3];
    int a,b;
    for(int i=0;i<3;i++){
        cin>>arr[i].first>>arr[i].second;
    }
    if(arr[0].first==arr[1].first){
        a=arr[2].first;
    }
    else if(arr[1].first==arr[2].first){
        a=arr[0].first;
    }
    else{
        a=arr[1].first;
    }
    if(arr[0].second==arr[1].second){
        b=arr[2].second;
    }
    else if(arr[1].second==arr[2].second){
        b=arr[0].second;
    }
    else{
        b=arr[1].second;
    }
    cout<<a<<" "<<b;
    return 0;
}