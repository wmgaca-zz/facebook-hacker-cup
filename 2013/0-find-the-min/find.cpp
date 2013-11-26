#include <stdio.h>
#include <vector>
#include <deque>
#include <map>
#include <math.h>
#include <algorithm>
#include <malloc.h>
#include <unordered_map>

using namespace std;

typedef unsigned long INT;
typedef deque<INT> VECT;
typedef unordered_map<INT, INT> MAP;

void printv(VECT* v) {
		printf("[");
		for (int i = 0; i < (int)v->size(); ++i) {
				printf("%lu, ", v->at(i));
		}
		printf("]\n");		
}

void gen(INT a, INT b, INT c, INT r, INT k, VECT* m, MAP* used) {
		INT val;

		m->push_back(a);
		(*used)[a] = 1;

		for (INT i=0; i<k; ++i) {
				val = (b * (*m)[m->size()-1] + c) % r;
				m->push_back(val);

				if (used->find(val) == used->end()) {
						(*used)[val] = 0;
				}
				(*used)[val] += 1;
		}
}

INT solve(INT n, INT k, INT a, INT b, INT c, INT r) {
		
		VECT* m = new VECT();
		MAP* used = new MAP();

		gen(a, b, c, r, k, m, used);

		VECT* unused = new VECT();
		for (INT x = 0; x < 2*k; ++x) {
				if (used->find(x) == used->end()) {
						unused->push_back(x);
				}
		}

		m->push_back((*unused)[0]);
		(*used)[(*unused)[0]] = 1;
		unused->pop_front();

		INT last = m->size() - 1;
		INT limit = 2 * k;
		INT currval;

		printf("limit = %lu\n", limit);

		while (last != 2 * k) {
				if (last % 100 == 0) {
						printf("%d %lu\n", m->size(), last);
						
				}
						
				currval = (*m)[0];

				if (unused->size() == 0) {
						printf("Big bad error (n=%lu, k=%lu)\n", n, k);
						return 0;
				}

				if (used->find(currval) == used->end()) {
						(*used)[currval] = 0;
				}
				
				if ((*used)[currval] == 0) {
						if (currval < (*unused)[0]) {
								m->push_back(currval);
								(*used)[currval] = 1;
						} else {
								m->push_back((*unused)[0]);
								(*used)[(*unused)[0]] = 1;
								unused->pop_front();
								unused->push_back(currval);
								sort(unused->begin(), unused->end());
						}
				} else if ((*used)[currval] > 1) {
						(*used)[currval] -= 1;
						m->push_back((*unused)[0]);
						unused->pop_front();
				} else if ((*used)[currval] == 1) {
						if (currval < (*unused)[0]) {
								m->push_back(currval);
						} else {
								(*used)[currval] = 0;
								m->push_back((*unused)[0]);
								(*used)[(*unused)[0]] = 1;
								unused->pop_front();
								unused->push_back(currval);
								sort(unused->begin(), unused->end());
								/*
								x = (*unused)[unused->size() - 1];
								while (true) {
										if (used->find(x) == used->end()) {
												unused->push_back(x);
												break;
										}
										++x;
								}// */		
						}
				}

				m->pop_front();
				++last;
		}
		printf("Done...\n");

		printf("m->size() = %lu\n", (INT)m->size()); 
		return m->back();
}

int main(void) {
		INT T;
		INT n, k;
		INT a, b, c, r;
		INT result;

		scanf("%lu", &T);

		for (INT t = 1; t <= T; ++t) {
				scanf("%lu %lu", &n, &k);
				scanf("%lu %lu %lu %lu", &a, &b, &c, &r);

				//if (t != 5) continue;

				printf("Solve #%lu\n", t);
				result = solve(n, k, a, b, c, r);
				printf("Case #%lu: %lu\n\n", t, result);
		}
		
		return 0;
}
