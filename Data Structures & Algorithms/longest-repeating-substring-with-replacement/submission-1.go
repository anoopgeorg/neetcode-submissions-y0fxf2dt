func characterReplacement(s string, k int) int {

    char_counter := make(map[byte]int)
    l := 0

    max_f := 0
    res := 0

    for r := range s{

        // Update the caracter count
        char_counter[s[r]]++

        // Update the max character frequency 
        if char_counter[s[r]] > max_f{
            max_f = char_counter[s[r]]
        }

        // Move window by one if # of substitutions does now match the delta 
        if (r-l+1) - max_f > k{
            char_counter[s[l]]--
            l++
        }

        // Update the res with the longest formed string
        if (r-l+1) > res{
            res = r-l +1
        }
    }
    return res
        

}
