#include<iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    int a;
    cin>>a;
    for(int i=0;i<a;i++)
    {
        int m,n;
        cin.tie(NULL);
        cin>>m>>n;
        cout<<m+n<<"\n";
    }
}