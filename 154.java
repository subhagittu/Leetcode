class Solution {
    public int findMin(int[] nums) {
        int low = 0, high = nums.length - 1;
        int mid = 0;
        int value = Integer.MAX_VALUE;
        while(low <= high) {
            mid = low + (high - low) / 2;
            value = Math.min(value, nums[mid]);

            if (nums[low] >= nums[mid] && nums[mid] > nums[high])
                low = mid + 1;
            else if (nums[low] < nums[mid] && nums[mid] <= nums[high]) 
                high = mid - 1;
            else if (nums[low] <= nums[mid] && nums[mid] > nums[high]) 
                low = mid + 1;
            else {
                int left = mid - 1, right = mid + 1;
                while (left >= 0 && right < nums.length && nums[left] == nums[right]) {
                    left--;
                    right++;
                }
                if (left >= 0 && right < nums.length && nums[left] < nums[right])
                    high = mid - 1;
                else 
                    low = mid + 1;
            }      
        }
        return value;
    }
}
