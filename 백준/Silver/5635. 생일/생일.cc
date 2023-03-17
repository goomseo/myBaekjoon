#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct profile{
    string name;
    int day, month, year;
};

bool compare(const struct profile& a, const struct profile& b);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    profile arr[101];
    for (int i = 0; i < n; i++)
        cin >> arr[i].name >> arr[i].day >> arr[i].month >> arr[i].year;

    sort(arr, arr + n, compare);

    cout << arr[n - 1].name << endl << arr[0].name << endl;

    return 0;
}

bool compare(const struct profile& a, const struct profile& b){
    if (a.year < b.year)
        return true;
    else if (a.year == b.year){
        if (a.month < b.month)
            return true;
        else if (a.month == b.month){
            if (a.day < b.day)
                return true;
            else
                return false;
        }
        else
            return false;
    }
    else
        return false;
}