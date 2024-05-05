#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool empty(vector<int> &v)
{
    return(!v.size());
}


void push(int x,vector<int> &v)
{
    v.push_back(x);
    return;
}

void pop(vector<int> &v)
{
    if(empty(v))
    {
        cout<<"-1"<<'\n';
        return; 
    }
    cout<<v.back()<<'\n';
    v.pop_back();
    return;        
}

void size(vector<int> &v)
{
    cout<<v.size()<<endl;
    return;
}

void top(vector<int> &v)
{
    if(empty(v))
    {
        cout<<"-1"<<'\n';
        return; 
    }
    cout<<v.back()<<endl;
    return;
}

int main()
{
    vector<int> v;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string str;
        cin>>str;
        if(str=="push")
        {
            int x;
            cin>>x;
            push(x,v);
        }
        else if(str=="pop")
        {
            pop(v);
        }
        else if(str=="size")
        {
            size(v);
        }
        else if(str=="empty")
        {
            cout<<empty(v)<<'\n';
        }
        else
        {
            top(v);
        }
    }
}