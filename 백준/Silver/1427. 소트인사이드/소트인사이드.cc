#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string num;
	cin >> num;

	sort(num.begin(), num.end());
	reverse(num.begin(), num.end());

	cout << num;

	return 0;
}