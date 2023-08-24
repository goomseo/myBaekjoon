#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m, k;

    cin >> n >> m;
    int matrix1[100][100] = {0};
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> matrix1[i][j];

    cin >> m >> k;
    int matrix2[100][100] = {0};
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < k; ++j)
            cin >> matrix2[i][j];

    int answer_matrix[100][100] = {0};
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < k; ++j) {
            for (int l = 0; l < m; ++l)
                answer_matrix[i][j] += matrix1[i][l] * matrix2[l][j];
            cout << answer_matrix[i][j] << " ";
        }
        cout << '\n';
    }
}
