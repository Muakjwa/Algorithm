#include<iostream>
#include<string>
using namespace std;

int main(){
    string s;
    cin>>s;
    for(int i=1;i<s.length()+1;i++){
        cout<<s.at(i-1);
        if(i%10==0){
            cout<<"\n";
        }
    }
    return 0;
}