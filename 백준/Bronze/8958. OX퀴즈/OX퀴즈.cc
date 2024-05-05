#include<iostream>
#include<string>
using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string s;
        int index=0,sum=0;
        cin>>s;
        for (int j=0;j<s.length();j++){
            if(s[j]=='O'){
                sum+=++index;
            }
            else{
                index=0;
            }
        }
        cout<<sum<<"\n";
    }
    return 0;
}