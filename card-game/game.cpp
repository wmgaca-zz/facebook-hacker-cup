#include <cstdio>
#include <cstring>
#include <map>
using namespace std;
#define MOD 1000000007
#define LL long long
#define N 10001

int n, k;
int vet[N];
map<int, int> m;
LL nck[N][N];

void pre()
{
	nck[0][0] = 1;
	for (int i = 1; i < N; ++i)
	{
		nck[i][0] = 1;
		for (int j = 1; j < N; ++j)
			nck[i][j] = (nck[i-1][j]+nck[i-1][j-1])%MOD;
	}
}

int main()
{
	pre();
	int t;
	scanf("%d", &t);
	printf("t=%d\n", t);
	for (int q = 1; q <= t; ++q)
	{
		printf("Case #%d: ", q);
		scanf("%d%d", &n, &k);
		m.clear();
		for (int i = 0; i < n; ++i)
			scanf("%d", &vet[i]), ++m[vet[i]];
		LL res = 0; int acc = 0;
		for (typeof(m.begin()) it = m.begin(); it != m.end(); ++it)
		{
			int a = it->first;
			LL b = it->second;
			res = (res+(a*nck[acc+b-1][k-1])%MOD)%MOD;
			acc += b;
		}
		printf("%lld\n", res);
	}
}
