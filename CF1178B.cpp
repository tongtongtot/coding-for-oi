// Problem: B. WOW Factor
// Contest: Codeforces - Codeforces Global Round 4
// URL: https://codeforces.com/problemset/problem/1178/B
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
// inline int read(){
	// int x=0,f=1;
	// char ch=getchar();
	// while('0'>ch||ch>'9'){
		// if(ch=='-') f=-1;
		// ch=getchar();
	// }
	// while('0'<=ch&&ch<='9'){
		// x=(x<<3)+(x<<1)+(ch^48);
		// ch=getchar();
	// }
	// return x*f;
// }
const int maxn = 1000005;
string str;
long long pre[maxn],suf[maxn];
signed main() {
	// ios::sync_with_stdio(false);
	// cin.tie(NULL); cout.tie(NULL);
	
	cin >> str;
	
	for(int i=1;i<str.size();i++){
		if (str[i] == 'v' && str[i-1] == 'v') pre[i] = pre[i-1] + 1;
		else pre[i] = pre[i-1];
	}
	for(int i=str.size()-2;i>-1;i--){
		if(str[i] == 'v' && str[i+1] == 'v') suf[i] = suf[i+1] + 1;
		else suf[i] = suf[i+1];
	}
	
	long long ans = 0;
	for(int i=1;i<str.size()-1;i++){
		if(str[i]=='o'){
			ans += pre[i] * suf[i];
		}
		// cout<<pre[i]<<" "<<suf[i]<<"\n";
	}
	
	
	cout<<ans<<"\n";
	return 0;
}