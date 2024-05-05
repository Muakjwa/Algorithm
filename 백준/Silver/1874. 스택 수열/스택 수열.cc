#include<iostream>
#include<stack>
#include<queue>
using namespace std;

int main(){
    int n;
    stack<int> tst,stk,real;
    queue<char> result;
    cin>>n;
    int a;
    for(int i=0;i<n;i++){
        cin>>a;
        tst.push(a);
    }
    for(int i=0;i<n;i++){
        stk.push(tst.top());
        tst.pop();
    }
    for(int i=1;i<n+1;i++){
        result.push('+');
        real.push(i);
        while(!real.empty()&!stk.empty()){
            if(real.top()==stk.top()){
                real.pop();
                stk.pop();
                result.push('-');
            }
            else{
                break;
            }
        }
    }
    if(!stk.empty() || !real.empty()){
        cout<<"NO";
    }
    else{
        while(!result.empty()){
            cout<<result.front()<<"\n";
            result.pop();
        }
    }
    return 0;
}