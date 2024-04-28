// #pragma GCC optimize(2)
#include <iostream>
#include <unordered_map>
using namespace std;
int a[100005],prime[10005],cnt,n,T;
bool st[100005];
unordered_map<int,bool> bigPrime;
void getPrime(){
    for(int i=2;i<=32000;i++){
        if (st[i] == false) prime[++cnt] = i;
        for(int j=1;j<=cnt && i*prime[j] <= 32000;j++){
            st[i*prime[j]] = true;
            if(i%prime[j] == 0) break;
        }
    }
}
bool solve(){
    for(int i=1;i<=n;i++){
    	// int x = a[i];
        for(int j=1;j<=cnt;j++){
        	if (prime[j]*prime[j] > a[i]){
        		break;
        	}
            if (a[i]%prime[j] == 0){
                if(bigPrime[prime[j]]) return true;
                bigPrime[prime[j]] = true;
                while(a[i]%prime[j] == 0){
                    a[i]/=prime[j];
                }
            }
        }
        if(a[i] > 1){
            if(bigPrime[a[i]]){
                return true;
            }
            bigPrime[a[i]] = true;
        }
    }
    return false;
}
int main(){
    ios::sync_with_stdio(false);
    // cin.tie(NULL); cout.tie(NULL);
    getPrime();
    // cout<<cnt<<endl;
    cin>>T;
    while(T--){
        bigPrime.clear();
        // memset(vis,0,sizeof(vis));
        cin>>n;
        for(int i=1;i<=n;i++){
            cin>>a[i];
        }
        bool ans = solve();
        if(ans) cout<<"YES\n";
        else cout<<"NO\n";    
    }
}