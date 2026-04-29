#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
    sort(arr.begin(), arr.end());
    vector<vector<int>> ans;
    int min_diff = INT_MAX;
    
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] - arr[i-1] < min_diff) {
            min_diff = arr[i] - arr[i-1];
        }
    }
    
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] - arr[i-1] == min_diff) {
            ans.push_back({arr[i-1], arr[i]});
        }
    }
    
    return ans;
}

int main() {
    vector<int> arr = {4, 2, 1, 3};
    vector<vector<int>> result = minimumAbsDifference(arr);
    
    for (auto& pair : result) {
        cout << "[" << pair[0] << ", " << pair[1] << "]" << endl;
    }
    
    return 0;
}