#include<iostream>
using namespace std;
int MAX=-1000000;
int MIN=1000000;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int a;
        cin>>a;
        if(a<MIN){
            MIN=a;
        }
        if(a>MAX){
            MAX=a;
        }
    }
    cout<<MIN<<" "<<MAX;
    return 0;
}