impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = Vec::new();
        for x in &nums {
            res.push(
                if let Some(i) = res.last() {
                    x+i
                } else {
                    *x
                })
        }
        res
    }
}