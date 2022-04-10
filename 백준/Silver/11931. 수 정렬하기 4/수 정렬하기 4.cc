#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> numbers;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int qtyNum;
	cin >> qtyNum;

	for (int i = 0; i < qtyNum; i++) {
		int num;
		cin >> num;
		numbers.push_back(num);
	}

	sort(numbers.begin(), numbers.end());
	reverse(numbers.begin(), numbers.end());

	for (int j = 0; j < qtyNum; j++) {
		cout << numbers[j] << '\n';
	}

	return 0;
}