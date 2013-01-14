#include <stdio.h>

void print_array(int* array, int array_sz) {
	int i;
	for (i = 0; i < array_sz; ++i) {
		printf("%d ", *(array + i));
	}
	printf("\n");
}

void print_array_addresses(int* begin, int* end) {
	if (begin > end) {
		return;
	}
	
	printf("%d\t%p\t%dB\n", *begin, begin, sizeof(*begin));

	return print_array_addresses(++begin, end);
}

void invert(int* begin, int* end) {
	if (begin >= end) {
		return;
	}

	*begin ^= *end;
	*end ^= *begin;
	*begin ^= *end;

	return invert(++begin, --end);
}

int strrindex(const char* s, char t) {
	int i = 0;
	int index = -1;
	char current;

	while (current = *(s + i)) {
		if (t == current) {
			index = i;
		}
		++i;
	}

	return index;
}

int main() {
	int array[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	int array_sz = 8;

	/*
	printf("%d", strrindex("Hello world", 'f'));
	*/
	/*
	print_array(&array[0], array_sz);
	print_array_addresses(&array[0], &array[array_sz - 1]);
	*/
	invert(&array[0], &array[array_sz - 1]);
	
	print_array(&array[0], array_sz);
	/*
	print_array_addresses(&array[0], &array[array_sz - 1]);
	*/

	return 0;
}
