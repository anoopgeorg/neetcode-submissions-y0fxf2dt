func maxProfit(prices []int) int {
    l,r := 0,1
    max_profit := 0

    for r < len(prices){
        if prices[r] > prices[l]{
            profit := prices[r] - prices[l]
            if profit > max_profit{
                max_profit = profit
            }
        } else {
            l = r
        }
        r++
    }
    return max_profit
}
