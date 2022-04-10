#include <iostream>
#include <algorithm>
using namespace std;

bool compare(const string& a, const string& b) {
	if (a.length() != b.length()) {
		return a.length() < b.length();
	}
	else {
		return a < b;
	}
}

string words[20001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int qtyWord;
	cin >> qtyWord;

	for (int i = 0; i < qtyWord; i++) {
		cin >> words[i];
	}

	sort(words, words + qtyWord, compare);

	for (int j = 0; j < qtyWord; j++) {
		if (words[j] != words[j + 1]) {
			cout << words[j] << '\n';
		}
	}

	return 0;
}