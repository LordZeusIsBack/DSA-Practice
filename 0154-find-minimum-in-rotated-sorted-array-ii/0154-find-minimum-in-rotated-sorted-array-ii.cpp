int speedup = []{ios::sync_with_stdio(0); cin.tie(0); return 0;}();


class Solution {
public:
    int findMin(vector<int>& nums) {
        return *min_element(nums.begin(), nums.end());
    }
};