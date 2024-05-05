#include<iostream>
#include<string>
using namespace std;

int main(){
    int n,t;
    cin>>t;
    string s;
    for(int k=0;k<t;k++){
        cin>>n>>s;
        for(int j=0;j<s.length();j++){
            for(int i=0;i<n;i++){
                cout<<s[j];
            }
        }
        cout<<"\n";
    }
    return 0;
}