#include<iostream>
#include<string>
using namespace std;

int main(){
    string s;
    int array[26]={0};
    cin>>s;
    for(int i=0;i<s.length();i++){
        if(s[i]>91){
            array[s[i]-'a']+=1;
        }
        else{
            array[s[i]-'A']+=1;
        }
    }
    int max=0,cnt=0;
    int max_index;
    for(int i=0;i<26;i++){
        if(max<array[i]){
            max=array[i];
            max_index=i;
        }
    }
    for(int i=0;i<26;i++){
        if(array[i]==max){
            cnt++;
        }
    }
    if(cnt>1){
        cout<<"?";
    }
    else{
        cout<<(char)(max_index+65);
    }
    return 0;
}