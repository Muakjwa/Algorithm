#include<iostream>
using namespace std;

int main(){
    for(int i=0;i<3;i++){
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        int sum=a+b+c+d;
        if(sum==4){
            cout<<"E"<<"\n";
        }
        else if(sum==1){
            cout<<"C"<<"\n";
        }
        else if(sum==2){
            cout<<"B"<<"\n";
        }
        else if(sum==3){
            cout<<"A"<<"\n";
        }
        else{
            cout<<"D"<<"\n";
        }
    }
    return 0;
}