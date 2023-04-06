#include <iostream>

using namespace std;

int main(){
    int arr[10] = {0};
    int max = 0;
    int maxIndex;

    for (int i = 0; i < 9; i++){
        cin >> arr[i];

        if (max < arr[i]){
            max = arr[i];
            maxIndex = i + 1;
        }
    }

    cout << max << endl<< maxIndex << endl;
}