class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> prevInts = new HashSet<Integer>();
        for (int i: nums) {
            if (prevInts.contains(i)) {
                return true;
            } else {
                prevInts.add(i);
            }
        }
        return false;
    }
}
