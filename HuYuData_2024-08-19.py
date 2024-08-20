class Solution {
public:
    int


largestRectangleArea(vector < int > & heights) {
    stack < int > stack;
int
max_area = 0;
int
index = 0;

while (index < heights.size()) {
if (stack.empty() | | heights[stack.top()] <= heights[index]) {
stack.push(index++);
} else {
int height = heights[stack.top()];
stack.pop();
int width = stack.empty() ? index: index - stack.top() - 1;
max_area = max(max_area, height * width);
}
}

while (!stack.empty()) {
int height = heights[stack.top()];
stack.pop();
int width = stack.empty() ? index: index - stack.top() - 1;
max_area = max(max_area, height * width);
}

return max_area;
}
};

// Example
usage:
vector < int > heights = {2, 1, 5, 6, 2, 3};
Solution
solution;
cout << solution.largestRectangleArea(heights) << endl; // Output: 10