#include <iostream>
#include <vector>
using namespace std;

int n, m;
bool visited[9];
vector <int> v;

void bt() {
	if (v.size() == m) {
		for (auto& k : v) {
			cout << k << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = v.back() + 1; i <= n; i++) {
		v.push_back(i);
		bt();
		v.pop_back();
		}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		v.push_back(i);
		bt();
		v.pop_back();
	}
	return 0;
}