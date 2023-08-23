#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

class Stack {
private:
    int arr[10001] = {0};
    int *p = arr;
    int size;

public:
    Stack() {this -> size = 0;}

    void push(int x) {
        *(p++) = x;
        size++;
    }

    void pop() {
        if (size == 0)
            cout << -1 << '\n';
        else {
            cout << *(--p) << '\n';
            *p = 0;
            size--;
        }
    }

    void getSize() {cout << size << '\n';}

    void empty() {
        if (size == 0)
            cout << 1 << '\n';
        else
            cout << 0 << '\n';
    }

    void top() {
        if (size == 0)
            cout << -1 << '\n';
        else {
            cout << *(--p) << '\n';
            p++;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    Stack s;

    int n;
    cin >> n;

    string command;
    int x;
    for (int i = 0; i < n; ++i) {
        cin >> command;

        if (command == "push") {
            cin >> x;
            s.push(x);
        }
        else if (command == "pop")
            s.pop();
        else if (command == "size")
            s.getSize();
        else if (command == "empty")
            s.empty();
        else
            s.top();
    }
}
