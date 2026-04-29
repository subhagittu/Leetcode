class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        List<List<Integer>> ans = new ArrayList<>();
        int minDiff = Integer.MAX_VALUE;
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i-1] < minDiff) {
                minDiff = arr[i] - arr[i-1];
            }
        }
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i-1] == minDiff) {
                ans.add(Arrays.asList(arr[i-1], arr[i]));
            }
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {4, 2, 1, 3};
        List<List<Integer>> result = solution.minimumAbsDifference(arr);
        System.out.println(result);
    }
}