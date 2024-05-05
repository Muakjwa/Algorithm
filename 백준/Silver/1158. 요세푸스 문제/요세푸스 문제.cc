#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int a,b;
    cin>>a>>b;
    int c=b-1;
    vector<int> vec;
    for(int i=1;i<=a;i++)
        vec.push_back(i);
    cout<<'<';
    while(vec.size())
    {
        cout<<vec[c];
        vec.erase(vec.begin()+c);
        if(vec.size())
            cout<<", ";
        c=c+b-1;
        c=c%vec.size();
    }
    cout<<'>';
}