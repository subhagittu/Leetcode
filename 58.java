class Solution {
    public int lengthOfLastWord(String s) { 
         s = s.trim(); // remove the spaces occuring at beginning and last
        int n = s.length();
        int count = 0;
        for(int i=n-1;i>=0;i--){
            if (s.charAt(i) == ' ') // if space encounter return from loop
            {
                return count;
            }
            else{
                count++;
            }
        }
        return count; // if string contains of only one word
    }
}
