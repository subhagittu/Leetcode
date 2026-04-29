#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;

class Solution {
public:
    long long numSub(string s) {
        long long result = 0;
        long long count = 0;
        
        for (char c : s) {
            if (c == '1') {
                count++;
                result = (result + count) % MOD;
            } else {
                count = 0;
            }
        }
        
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.numSub("1001101") << endl;  // Output: 6
    cout << sol.numSub("111") << endl;      // Output: 3
    cout << sol.numSub("1") << endl;        // Output: 1
    return 0;
}
