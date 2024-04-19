import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution { 
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums); 
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        helper(nums, (long) target, 0, result, temp, 4); 
        return result;
    }

    private void helper(int[] nums, long target, int start, List<List<Integer>> result, List<Integer> temp, int numNeed) {
        if (numNeed != 2) {
            for (int i = start; i < nums.length - numNeed + 1; i++) {
                if (i > start && nums[i] == nums[i - 1]) {
                    continue; 
                }
                temp.add(nums[i]); 
                helper(nums, target - nums[i], i + 1, result, temp, numNeed - 1); 
                temp.remove(temp.size() - 1); 
            }
            return;
        }

      
        int l = start;
        int r = nums.length - 1;
        while (l < r) {
            long total = (long) nums[l] + nums[r];
            if (total < target) {
                l++;
            } else if (total > target) {
                r--;
            } else {
                temp.add(nums[l]); 
                temp.add(nums[r]); 
                result.add(new ArrayList<>(temp)); 
                temp.remove(temp.size() - 1); 
                temp.remove(temp.size() - 1); 
                l++;
                r--;
                while (l < r && nums[l] == nums[l - 1]) {
                    l++; 
                }
            }
        }
    }
}
