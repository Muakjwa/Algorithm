#include<iostream>
using namespace std;

int main(){
    int n;
    int max=0;
    cin>>n;
    int array[10]={0};
    while(n!=0){
        array[n%10]+=1;
        n/=10;
    }
    array[6]+=array[9];
    array[9]=0;
    array[6]=array[6]/2+array[6]%2;
    for(int i=0;i<10;i++){
        if(max<array[i]){
            max=array[i];
        }
    }
    cout<<max;
    return 0;
}