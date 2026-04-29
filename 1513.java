class Solution {
    private static final long MOD = 1000000007L;
    
    public int numSub(String s) {
        long result = 0;
        long count = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '1') {
                count++;
                result = (result + count) % MOD;
            } else {
                count = 0;
            }
        }
        
        return (int) result;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.numSub("1001101"));  // Output: 6
        System.out.println(sol.numSub("111"));      // Output: 3
        System.out.println(sol.numSub("1"));        // Output: 1
    }
}
