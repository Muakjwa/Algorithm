#include<iostream>
#include<string>
using namespace std;

int main(){
    string a,b;
    cin>>a;
    while(a!="0"){
        for(int i=0;i<a.length();i++){
            b.push_back(a[a.length()-i-1]);
        }
        if(a==b){
            cout<<"yes"<<"\n";
        }
        else{
            cout<<"no"<<"\n";
        }
        b.clear();
        cin>>a;
    }
    return 0;
}