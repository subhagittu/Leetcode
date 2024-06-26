class Solution {
    public int compareVersion(String version1, String version2) {
        String[] a = version1.split("\\."), b = version2.split("\\.");
        boolean changed = false; 
        if (a.length < b.length) {
            String[] temp = a; 
            a = b;
            b = temp;
            changed = true;
        }
        for (int i = 0; i < a.length; i++) {
            String one = removeLeadingZeros(a[i]), two = i >= b.length ? "0" : removeLeadingZeros(b[i]);
            if (!one.equals(two)) {
                if (one.length() > two.length()) return changed ? -1 : 1;
                else if (one.length() < two.length()) return changed? 1 : -1;
                else {
                    for (int j = 0; j < one.length(); j++) {
                        if (one.charAt(j) > two.charAt(j)) return changed ? -1 : 1;
                        else if (one.charAt(j) < two.charAt(j)) return changed ? 1 : -1;
                    }
                }
            }
        }
        return 0;
    }

    private static String removeLeadingZeros(String s) {
        for (int i = 0; i < s.length(); i++) if (s.charAt(i) != '0') return s.substring(i);
        return "0";
    }
}
