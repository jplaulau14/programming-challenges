class Solution {
	public:
		bool containsDuplicate(vector<int>& nums) {
			int size = nums.size();
			int set_size = set<int>(nums.begin(), nums.end()).size();
			return size > set_size;
		}
};
