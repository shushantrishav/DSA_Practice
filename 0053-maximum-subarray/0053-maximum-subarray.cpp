class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentsum = nums[0];
        int maxi = nums[0];
        if (nums.size() == 0){
            return -1;
        }
        for(int i = 1 ; i < nums.size(); i++){
            currentsum = max(nums[i], currentsum + nums[i] );
            maxi = max(maxi , currentsum);
        }
        return maxi;
    }
};