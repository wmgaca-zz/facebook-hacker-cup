#include <stdio.h>

void print_array(int* array, int array_sz) {
	int i;
	for (i = 0; i < array_sz; ++i) {
		printf("%d ", *(array + i));
	}
	printf("\n");
}

void move_left(int* array, int array_sz) {
	int i;
	int last;

	for (i = 0, last = 0; i < array_sz; ++i) {
		if (array[i] != 0) {
			if (last != i) {
				array[last] = array[i];
				array[i] = 0;
			}
			++last;
		}
    }
}

int main() {
	int array[] = {1, 2, 8, 0, 0, 4, 0, 6, 0};
	int array_sz = sizeof(array) / sizeof(int);

    print_array(&array[0], array_sz);

	move_left(array, array_sz);

	print_array(&array[0], array_sz);

	return 0;
}
