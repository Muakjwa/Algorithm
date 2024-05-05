#include<iostream>
using namespace std;

int main(){
    int array[15][15]={0};
    for(int i=0;i<15;i++){
        array[0][i]=i;
    }
    for(int i=1;i<15;i++){
        for(int j=0;j<15;j++){
            for(int k=0;k<=j;k++){
                array[i][j]+=array[i-1][k];
            }
        }
    }
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int k,n;
        cin>>k>>n;
        cout<<array[k][n]<<"\n";
    }
    return 0;
}