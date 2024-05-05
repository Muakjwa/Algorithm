#include<iostream>
#include<queue>
#include<memory.h>
#include<algorithm>
using namespace std;

int arr[1001][1001];
int visit[1001];
int N,M,V;
int u,v;

void dfs(int x)
{
    int i=0;
    visit[x]=1;
    cout<<x<<" ";
    
    for(i=1;i<=N;i++)
    {
        if(arr[x][i]==1&&visit[i]==0)
        {
            dfs(i);
        }
    }
    if(i==N) return;
}

void bfs(int x)
{
    queue<int> q;
    q.push(x);
    while(!q.empty())
    {
        int next_x=q.front();
        visit[next_x]=1;
        cout<<next_x<<" ";
        q.pop();
        
        for(int i=1;i<=N;i++)
            if(arr[next_x][i]==1&&visit[i]==0)
            {
                q.push(i);
                visit[i]=1;
            }
    }
}

int main()
{
    cin>>N>>M>>V;
    for(int i=0;i<M;i++)
    {
        cin>>u>>v;
        arr[u][v]=1;
        arr[v][u]=1;
    }
    dfs(V);
    cout<<endl;
    memset(visit,0,sizeof(visit));
    
    bfs(V);
}