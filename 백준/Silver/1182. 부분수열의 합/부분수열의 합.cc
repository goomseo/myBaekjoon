#include <iostream>
using namespace std;

int N, S, ans, sum;
int arr[21];

void bt(int idx) {
	if (idx == N) {
		return;
	}

	sum += arr[idx];
	if (sum == S) {
		ans++;
	}

	bt(idx + 1);
	sum -= arr[idx];
	bt(idx + 1);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> S;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	bt(0);
	cout << ans;
	
	return 0;
}