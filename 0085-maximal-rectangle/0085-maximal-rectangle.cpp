class Solution {
private:
    int helper(vector<int>& heights) {
        int n = heights.size();
        stack<int> st;
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!st.empty() && h < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                maxArea = max(maxArea, height * width);
            }
            st.push(i);
        }
        return maxArea;
    }

public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty())
            return 0;

        int maxArea = 0;
        int cols = matrix[0].size();
        vector<int> heights(cols, 0);

        for (auto& row : matrix) {
            for (int j = 0; j < cols; j++) {
                heights[j] = (row[j] == '1') ? heights[j] + 1 : 0;
            }
            maxArea = max(maxArea, helper(heights));
        }
        return maxArea;
    }
};