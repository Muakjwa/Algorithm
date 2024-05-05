#include<iostream>
#include<string>
using namespace std;

int main(){
    char carr[8][8];
    int iarr[8][8];
    int cnt=0;
    for(int i=0;i<64;i++){
        if(((i/8)%2==0 and i%2==0) or ((i/8)%2==1 and i%2==1)){
            iarr[i/8][i%8]=0;
        }
        else{
            iarr[i/8][i%8]=1;
        }
    }
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            cin>>carr[i][j];
            if(carr[i][j]=='F' and iarr[i][j]==0){
                cnt+=1;
            }
        }
    }
    cout<<cnt;
    return 0;
}