class Solution {
    public int divide(int dividend, int divisor) {
        long ans = (long)dividend/divisor;
    if(ans>Integer.MAX_VALUE) return Integer.MAX_VALUE;
    else if(ans<Integer.MIN_VALUE) return Integer.MIN_VALUE;
    else return (int)ans;
    }
}
