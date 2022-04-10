#include <iostream>
#include <algorithm>
using namespace std;

struct prsnInfo {
	int joinOrder, age;
	string name;
}prsnInfoArr[100001];

bool compare(prsnInfo& a, prsnInfo& b) {
	if (a.age != b.age) {
		return a.age < b.age;
	}
	else {
		return a.joinOrder < b.joinOrder;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int qtyMember;
	cin >> qtyMember;

	for (int i = 0; i < qtyMember; i++) {
		cin >> prsnInfoArr[i].age >> prsnInfoArr[i].name;
		prsnInfoArr[i].joinOrder = i;
	}

	sort(prsnInfoArr, prsnInfoArr + qtyMember, compare);

	for (int j = 0; j < qtyMember; j++) {
		cout << prsnInfoArr[j].age << ' ' << prsnInfoArr[j].name << '\n';
	}

	return 0;
}