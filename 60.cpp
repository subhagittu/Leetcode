class Solution {
public:
    string s = "";
    int fact(int f){
        if(f==1) return 1;
        return f*fact(f-1);
    }
    void getSeq(int n, int k, vector<int>v, int start, int end){
        if(n==0) return;
        int range = end-start+1;
        int currrange = range/n;
        for(int i=1; i<=n; i++){
            int lower = start + (i-1)*currrange;
            int higher = lower + currrange - 1;
            if(k>=lower && k<=higher){
                s.append(to_string(v[i-1]));
                auto it = find(v.begin(), v.end(), v[i-1]);
                v.erase(it);
                getSeq(n-1, k, v, lower, higher);
            }
        }
    }
    string getPermutation(int n, int k) {
        vector<int> v;
        for(int i=0; i<n; i++){
            v.push_back(i+1);
        }
        int start = 1;
        int end = fact(n);
        getSeq(n,k,v, start, end);
        return s;
    }
};
