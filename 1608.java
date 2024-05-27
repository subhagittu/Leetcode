class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);


            int start = 0;
            int end = nums.length;

            while(start<=end){

                    int mid = start+ (end-start)/2;
                    int ans = count(nums, mid);
                   
                    if(ans == mid) return mid;
                    else if(ans>mid)    start = mid+1;
                    else end = mid-1;


            }
            
        
        return -1;
    }
    int count(int []nums, int target){
            int ans = 0;
            for(int num : nums){
                if(num>=target) ans++;
                
            }
        return ans;
    }


}
