class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum=Integer.MAX_VALUE;
        for(int i=0;i<nums.length-2;i++){
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
            int sum=nums[i]+nums[j]+nums[k];
             if (Math.abs(target - sum) < Math.abs(target - closestSum)) {
                    closestSum = sum; 
                }
            if(sum>target) k--;
            else j++;
            }
        }
        return closestSum;
    }
}
