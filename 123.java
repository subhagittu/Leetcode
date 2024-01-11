class Solution {

    static int dp[][][];
    static int helper(int arr[], int i, int k, int flag){
        if(i==arr.length) return 0;

        if(dp[flag][k][i]!=-1) return dp[flag][k][i]; 

        int ans = Integer.MIN_VALUE;
        ans = helper(arr,i+1,k,flag);   // leave thar stock

        if(flag==1){
            ans = Math.max(ans, helper(arr,i+1,k-1,0)+arr[i]);  // sell
        }else{
            if(k>0) ans = Math.max(ans,helper(arr,i+1,k,1)-arr[i]);  // buy
        }
        return  dp[flag][k][i] = ans;
    }
    public int maxProfit(int[] arr) {
        dp = new int[2][3][100005];
        for(var a : dp){
            for(var b : a) Arrays.fill(b,-1);
        }
        
        return helper(arr,0,2,0);
    }
}
