impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        if s.len() == 0 {
            return true;
        }
        let mut base: Vec<char> = s.chars().collect();
        let mut t_chars = t.chars();
        let mut counter = 0;
        for i in 0..t.len() {
            let t_cur = t_chars.next();
            if t_cur.unwrap() == base[counter] {
                counter += 1;
                if counter == s.len() {
                    return true;
                }
            }
        }
        return false;
    }
}