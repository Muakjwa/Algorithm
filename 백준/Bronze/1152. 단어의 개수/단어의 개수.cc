#include<iostream>
#include<string>
using namespace std;

int main(){
    string s;
    int val=1;
    getline(cin,s);
    if(s.empty()){
        cout<<0;
        return 0;
    }
    if(s[0]==' '){
        val-=1;
    }
    if(s[s.length()-1]==' '){
        s.pop_back();
    }
    while(s.length()!=0){
        if(s[s.length()-1]==' '){
            val+=1;
        }
        s.pop_back();
    }
    cout<<val;
    return 0;
}