#include <iostream>
using namespace std;

int main() {
    #ifdef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int savings;
    cin >> savings;
    if (savings > 5000) {
        cout << "Neha\n";
    } else {
        cout << "Rashmi\n";
    }

    return 0;
}