#include <iostream>
#include <string>
using namespace std;

struct playerInfo{
    int value;
    string name;
};

int main(){
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int p;
        cin >> p;
        playerInfo playerArr[101] = {0};

        int max = 0;
        string answer;
        for (int j = 0; j < p; j++){
            cin >> playerArr[j].value >> playerArr[j].name;
            if (max < playerArr[j].value){
                max = playerArr[j].value;
                answer = playerArr[j].name;
            }
        }
        
        cout << answer << endl;
    }

    return 0;
}