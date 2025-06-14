class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<int> curr(n, 0), next(n, 0);

        for (int i = n - 1; i >= 0; --i) {
            curr[i] = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j])
                    curr[j] = 2 + next[j - 1];
                else
                    curr[j] = max(next[j], curr[j - 1]);
            }
            next = curr;
        }
        return curr[n - 1];
    }
};