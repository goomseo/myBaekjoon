#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    double score[1001] = {0};
    double max = 0;
    for (int i = 0; i < n; i++) {
        cin >> score[i];

        if (max < score[i])
            max = score[i];
    }

    double sum = 0.0;
    for (int i = 0; i < n; i++)
        sum += score[i] / max * 100;

    cout << sum / n << endl;

    return 0;
}