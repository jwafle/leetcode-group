class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = 1;
        for (int i = 1; i < result.length; i++) {
            result[i] = result[i-1] * nums[i-1];
        }
        int postfix = 1;
        for (int i = result.length-2; i >= 0; i--) {
            postfix = nums[i+1] * postfix;
            result[i] = result[i] * postfix;
        }
        return result;
    }
}
