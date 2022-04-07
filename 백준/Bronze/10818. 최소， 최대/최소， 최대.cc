#include <iostream>
#include <vector>
using namespace std;

int intArr[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int qtyInt;
	cin >> qtyInt;

	for (int i = 0; i < qtyInt; i++) {
		cin >> intArr[i];
	}

	int minInt = 1000000;
	int maxInt = -1000000;
	for (int j = 0; j < qtyInt; j++) {
		if (intArr[j] < minInt) {
			minInt = intArr[j];
		}
		if (intArr[j] > maxInt) {
			maxInt = intArr[j];
		}
	}

	cout << minInt << " " << maxInt;

	return 0;
}