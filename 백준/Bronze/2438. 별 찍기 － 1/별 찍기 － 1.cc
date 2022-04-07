#include <iostream>
#include <vector>
using namespace std;

int main() {
	int line;
	cin >> line;

	for (int i = 0; i < line; i++) {
		for (int j = 0; j < i + 1; j++) {
			cout << "*";
		}
		cout << "\n";
	}
	return 0;
}