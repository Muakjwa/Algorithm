#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin>>n;
    
    vector<string> name(n);
    vector<pair<int,int>> age(n);
    
    for(int i=0;i<n;i++)
    {
        cin>>age[i].first>>name[i];
        age[i].second=i;
    }
    
    sort(age.begin(),age.end());
    
    for(int i=0;i<age.size();i++)
    {
        cout<<age[i].first<<" "<<name[age[i].second]<<'\n';
    }
}