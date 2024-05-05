#include<iostream>
#include<memory.h>
#include<algorithm>
using namespace std;

int visit[1001][1001];
int visited[1001];
int N,M,a,b,cnt=0;

void dfs(int x)
{
    visited[x]=1;
    int i=0;
    for(i=1;i<=N;i++)
        if(visit[x][i]==1&&visited[i]==0)
        {
            dfs(i);
        }
    if(i==N)
        return;
}

int main()
{
    cin>>N>>M;
    for(int i=1;i<=M;i++)
    {
        cin>>a>>b;
        visit[a][b]=1;
        visit[b][a]=1;
    }
    memset(visited,0,sizeof(visited));
    for(int i=1;i<=N;i++)
    {
        if(visited[i]==0)
        {
            dfs(i);
            cnt+=1;
        }
    }
    cout<<cnt;
}