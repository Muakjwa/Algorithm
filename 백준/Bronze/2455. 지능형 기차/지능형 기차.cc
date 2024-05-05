#include<iostream>
using namespace std;

int main(){
    int ans=0,sum=0;
    for(int i=0;i<4;i++){
        int a,b;
        cin>>a>>b;
        sum+=(b-a);
        if(ans<sum){
            ans=sum;
        }
    }
    cout<<ans;
}