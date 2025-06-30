class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty())
            return 0;

        int m = grid.size();
        int n = grid[0].size();
        int islands = 0;

        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        auto bfs = [&](int x, int y) {
            queue<pair<int, int>> q;
            q.push({x, y});
            grid[x][y] = '0'; // mark as visited

            while (!q.empty()) {
                auto [i, j] = q.front();
                q.pop();

                for (auto [di, dj] : directions) {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
                        grid[ni][nj] == '1') {
                        q.push({ni, nj});
                        grid[ni][nj] = '0'; // mark as visited
                    }
                }
            }
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++islands;
                    bfs(i, j);
                }
            }
        }

        return islands;
    }
};
