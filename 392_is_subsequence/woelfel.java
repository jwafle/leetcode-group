class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) {
            return true;
        } else if (t.length() == 0) {
            return false;
        }
        Queue<Character> q = new LinkedList<>(); 
        for (int i = 0; i < s.length(); i++) {
            q.add(s.charAt(i));
        }
        for (int i = 0; i < t.length(); i++) {
            if (q.peek() == t.charAt(i)) {
                q.remove();
            }
            if (q.size() == 0) {
                return true;
            }
        }
       
        return false;
    }
}
