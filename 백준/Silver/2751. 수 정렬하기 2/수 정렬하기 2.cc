#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int numbers[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
	}

	sort(numbers, numbers + n);

	for (int j = 0; j < n; j++) {
		cout << numbers[j] << "\n";
	}

	return 0;
}