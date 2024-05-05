#include<iostream>
using namespace std;

int main(){
    int index=0,max=0;
    for(int i=1;i<10;i++){
        int t;
        cin>>t;
        if(t>max){
            index=i;
            max=t;
        }
    }
    cout<<max<<"\n"<<index;
    return 0;
}