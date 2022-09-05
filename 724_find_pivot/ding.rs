impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut right: i32 = nums.iter().sum();
        let mut left: i32 = 0;
        for (i, n) in nums.iter().enumerate() {
            right -= n;
            if left == right {
                return i as i32
            }
            left += n;
        }
        -1
    }
}
