class Solution {
    public int maxProfit(int[] prices) {
        
        int price = prices[0];
        int profit = 0;
        int maxprofit = 0;
        
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > price) {
                profit = prices[i] - price;
                maxprofit = Math.max(maxprofit, profit);
            } else {
                price = prices[i];
            }
        }
        return maxprofit;
    }
}
