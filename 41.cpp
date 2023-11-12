class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        set<int> data;
        int n=nums.size();
        for(int x=0;x<n;x++)
        {
            data.insert(nums[x]);
        }
        int i=1;
        while(i<=n)
        {
            if(data.find(i)!=data.end()) i++;
            else return i;
        }
        return i;
    }
};
