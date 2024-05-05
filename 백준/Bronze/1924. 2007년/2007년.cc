#include<iostream>
#include<string>
using namespace std;

int main(){
    int a,b,day=0;
    cin>>a>>b;
    int arr[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    string yo[7]={"SUN","MON","TUE","WED","THU","FRI","SAT"};
    for(int i=1;i<a;i++)
    {
        day+=arr[i];
    }
    day+=b;
    cout<<yo[day%7];
}