#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<vector<int>> arr(n,vector<int>(2,0));
    vector<vector<int>> rev(n,vector<int>(2,0));
    for(int i=0;i<n;i++)
    {
        cin>>rev[i][1];
        cin>>rev[i][0];
    }
    
    sort(rev.begin(),rev.end());
    
    for(int i=0;i<rev.size();i++)
    {
        cout<<rev[i][1]<<" "<<rev[i][0]<<'\n';
    }
}