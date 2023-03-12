class Solution {
 public:
  vector<int> leftRigthDifference(vector<int>& nums) {
    vector<int> ans;
    int leftSum = 0;
    int rightSum = accumulate(begin(nums), end(nums), 0);

    for (const int num : nums) {
      rightSum -= num;
      ans.push_back(abs(leftSum - rightSum));
      leftSum += num;
    }

    return ans;
  }
};
