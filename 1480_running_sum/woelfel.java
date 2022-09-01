class Solution {
    public int[] runningSum(int[] nums) {
        int[] runningSum = new int[nums.length];
        int totalSum = 0;
        for (int i = 0; i < nums.length; i++) {
            totalSum = totalSum + nums[i];
            runningSum[i] = totalSum;
        }
        return runningSum;
    }
}
