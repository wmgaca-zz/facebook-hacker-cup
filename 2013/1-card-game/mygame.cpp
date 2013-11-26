#include <stdio.h>
#include <vector>
#include <algorithm>

#define REP(k,a,b) for(typeof(b) k=(a); k < (b); ++k)

using namespace std;

typedef unsigned long long ULL;

ULL MAX = 1000000007;

int main(void) {
		ULL T, result, N, K, temp, c;
		scanf("%llu", &T);
		vector<ULL> v;

		REP(t, 1, T+1) {
				result = 0;
				scanf("%llu %llu", &N, &K);
				REP(n, 0, N) {
						scanf("%llu", &temp);
						v.push_back(temp);
				}

				sort(v.begin(), v.end());

				c = 1L;
				result = v[K-1];

				REP(x, K, N) {
						c *= x;
						c /= x - (K-1);
						c %= MAX;
						result += (v[x] * c) % MAX;
						result %= MAX;
				}

				printf("Case #%llu: %llu\n", t, result);
		}

}
