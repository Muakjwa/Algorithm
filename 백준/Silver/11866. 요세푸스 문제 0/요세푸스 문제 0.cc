#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    int t=0;
    vector<int> stk,result;
    for(int i=1;i<n+1;i++){
        stk.push_back(i);
    }
    while(!stk.empty()){
        t=t+k-1;
        if(t>=stk.size()){
            t%=stk.size();
        }
        result.push_back(stk[t]);
        stk.erase(stk.begin()+t);
    }
    cout<<"<";
    while(result.size()>1){
        cout<<result[0]<<", ";
        result.erase(result.begin());
    }
    cout<<result[0]<<'>';
    return 0;
}