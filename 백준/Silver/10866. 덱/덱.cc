#include<iostream>
#include<vector>
#include<string>
using namespace std;
vector<int> v;

void puf(int a){
    v.insert(v.begin(),a);
}
void pub(int a){
    v.push_back(a);
}
void pof(){
    if(v.size()){
        cout<<v[0]<<'\n';
        v.erase(v.begin());
    }
    else{
        cout<<-1<<'\n';
    }
}
void pob(){
    if(v.size()){
        cout<<v[v.size()-1]<<'\n';
        v.pop_back();
    }
    else{
        cout<<-1<<'\n';
    }
}
void size(){
    cout<<v.size()<<'\n';
}
void empty(){
    cout<<v.empty()<<'\n';
}
void fr(){
    if(v.size()){
        cout<<v[0]<<'\n';
    }
    else{
        cout<<-1<<'\n';
    }
}
void ba(){
    if(v.size()){
        cout<<v[v.size()-1]<<'\n';
    }
    else{
        cout<<-1<<'\n';
    }
}


int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        if(s=="push_back"){
            int a;
            cin>>a;
            pub(a);
        }
        else if(s=="push_front"){
            int a;
            cin>> a;
            puf(a);
        }
        else if(s=="pop_front"){
            pof();
        }
        else if(s=="pop_back"){
            pob();
        }
        else if(s=="size"){
            size();
        }
        else if(s=="empty"){
            empty();
        }
        else if(s=="front"){
            fr();
        }
        else if(s=="back"){
            ba();
        }
    }
}