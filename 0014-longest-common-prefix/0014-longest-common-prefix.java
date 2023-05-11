class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String str1 = strs[0];
        String str2 = strs[strs.length-1];
        int indx = 0;
        while(indx < str1.length() && indx < str2.length()){
            if(str1.charAt(indx) == str2.charAt(indx)){
                indx++;
            } else {
                break;
            }
        }
        return str1.substring(0, indx);
    }
}

