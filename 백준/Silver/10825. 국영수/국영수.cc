#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

struct STU{
    string name;
    int kor,eng,math;
};

bool cmp(STU a, STU b)
{
    if(a.kor==b.kor&&a.eng==b.eng&&a.math==b.math) return a.name<b.name;
    if(a.kor==b.kor&&a.eng==b.eng) return a.math>b.math;
    if(a.kor==b.kor) return a.eng<b.eng;
    return a.kor>b.kor;
}

int main(){
    int n;
    cin>>n;
    
    vector<STU> v(n);
    for(int i=0;i<n;i++)
        cin>>v[i].name>>v[i].kor>>v[i].eng>>v[i].math;
    sort(v.begin(),v.end(),cmp);
    
    for(int i=0;i<n;i++)
        cout<<v[i].name<<'\n';
}