#include<iostream>
#include<queue>
using namespace std;

int main(){
    
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    int n;
    cin>>n;
    priority_queue<int,vector<int>, greater<int>> q;
    for(int i=0;i<n;i++){
        int k;
        cin>>k;
        if(k==0){
            if(q.size()){
                cout<<q.top()<<"\n";
                q.pop();
            }
            else{
                cout<<0<<'\n';
            }
        }
        else{
            q.push(k);
        }
    }
    return 0;
}