use std::collections::HashMap;

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut s_map = HashMap::new();
        let mut t_map = HashMap::new();
        let mut s_chars = s.chars();
        let mut t_chars = t.chars();
        let mut s_counter = 0;
        let mut t_counter = 0;

        for i in 0..s.len() {
            let s_cur = s_chars.next();
            let t_cur = t_chars.next();
            
            if !s_map.contains_key(&s_cur) {
                s_map.insert(s_cur, s_counter);
                s_counter += 1;
            }
            if !t_map.contains_key(&t_cur) {
                t_map.insert(t_cur, t_counter);
                t_counter += 1;
            }

            if s_map[&s_cur] != t_map[&t_cur] {
                return false;
            }
        }
        return true;
    }
}