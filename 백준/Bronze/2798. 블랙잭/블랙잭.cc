#include <iostream>
#include <vector>
using namespace std;

int cardNum[101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int qtrCard, goal;
	cin >> qtrCard >> goal;

	for (int i = 0; i < qtrCard; i++) {
		cin >> cardNum[i];
	}

	int sumResult = 0;
	for (int j = 0; j < qtrCard - 2; j++) {
		for (int k = j + 1; k < qtrCard - 1; k++) {
			for (int l = k + 1; l < qtrCard; l++) {
				if (sumResult <= cardNum[j] + cardNum[k] + cardNum[l] && cardNum[j] + cardNum[k] + cardNum[l] <= goal) {
					sumResult = cardNum[j] + cardNum[k] + cardNum[l];
				}
			}
		}
	}

	cout << sumResult;

	return 0;
}