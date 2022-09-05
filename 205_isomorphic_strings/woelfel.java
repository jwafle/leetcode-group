class Solution {
    public boolean isIsomorphic(String s, String t) {
        char[] l = s.toCharArray();
        char[] m = t.toCharArray();
        HashMap<Character, Character> mappedChars = new HashMap<Character, Character>();
        
        for (int i = 0; i < l.length; i++) {
            if (mappedChars.containsKey(l[i])) {
                if (mappedChars.get(l[i]) != m[i]) {
                    return false;
                }
            }
            else if (mappedChars.containsValue(m[i])) {
                return false;
            }
            mappedChars.put(l[i],m[i]);
        }
        return true;
    }
}
