func lengthOfLongestSubstring(s string) int {
    charset := make(map[byte]struct{})
    l := 0
    max_len := 0
    
    for r := range s{
        for{
            _,ok := charset[s[r]]
            if !ok{
                break
            }
            delete(charset,s[l])
            l++
        }
        charset[s[r]] = struct{}{}
        if (r-l+1) > max_len{
            max_len = r-l+1
        }
    } 
    return max_len
}
