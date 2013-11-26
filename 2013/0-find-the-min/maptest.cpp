#include <map>
#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
	map<int, int>* m = new map<int, int>();
	if (m->find(5) != m->end()) {
		printf("YEP!");
	} else {
		printf("NOPE!");
	}
	return 0;
}
