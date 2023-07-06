#include <iostream>
using namespace std;

int Fibonacci(int n){
    int arr[3] = {0,1,1};
    for(int i=2 ; i<n; i++){
        arr[(i+1)%3] = arr[i%3] + arr[(i-1)%3];
    }
    return arr[n%3];
}
 
int main(void){
    int num;
    cin >> num;
    cout << Fibonacci(num);
    
    return 0;
}