class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) 
{
        int n = triangle.size(); 
        vector<vector<int>> dp = triangle ;
        for(int i = 0 ;i < n-1 ; i++){
            for(int j = 0 ; j < dp[i].size(); j++){
                dp[i][j] = 0 ;
                cout<<dp[i][j]<<" "; 
            }cout<<endl;
        }
        for(int i = n-2 ;i >=0 ; i--){
            for(int j = 0 ; j < dp[i].size(); j++){
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]; 
            }
        }
        return dp[0][0] ;
    }
};
