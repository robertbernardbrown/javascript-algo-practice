var findMaxSlidingWindow = function (nums, windowSize) {
    let window = [];
    let result = [];

    if (windowSize === 0 || nums.length === 0) {
        return result;
    }

    if (windowSize > nums.length) {
        windowSize = nums.length;
    }

    for (let i = 0; i < windowSize; i++) {
        while(window.length && nums[i] > nums[windowSize[windowSize.length - 1]]) {
            window.pop();
        }
        window.push(i);
    }

    result.push(nums[window[0]]);

    for (let i = windowSize; i < nums.length; i++) {
        if (window.length && window[0] <= i - windowSize) {
            window.shift();
        }
        while(window.length && nums[i] >= nums[windowSize[windowSize.length - 1]]) {
            window.pop();
        }
        window.push(i);
        result.push(nums[window[0]]);
    }

    return result;
};

// Time complexity
// The input parameters of the function are an array of integers, and an integer specifying the size of the window. To get a clearer understanding of the time complexity of our solution, we need to consider the different ways in which the values in the input array change. The values in the array can be:

// Strictly increasing
// Strictly decreasing
// Constant
// Mixed, for example, increasing, decreasing, constant, then decreasing again, then constant, then increasing, then constant and then decreasing
// On the surface, we might expect our solution to take O(n * w)
// O(n∗w)
// , but that would be no better than the naive solution. When we look closer at our solution, it comes down to figuring out how many times the clean-up loop actually runs. This is the loop that pops all elements from the deque that are smaller than the new element in the window.

// Let’s consider the first case, that is, when the values in the array are strictly increasing. The first time the window moves forward, the new element is larger than all the other elements in the deque, so we have to perform the pop() operation w
// w
//  times, where w
// w
//  is the size of the window. Then, in all the subsequent steps, the pop() operation is performed only once, as the deque will only contain one element from this point onwards. So, the complexity in this case is O(w + n)
// O(w+n)
// , where n
// n
//  is the size of the array of integers.

// In the second case, every time the window moves forward, the new element is smaller than all the other elements in the deque, so the shift() operation is only performed once in every subsequent step, to remove the element which does not fall in the window anymore. So, again the time complexity is O(n)
// O(n)
// .

// In the third case, the same behaviour is repeated as in the second case, so the time complexity is O(n)
// O(n)
//  here too.

// Finally, in the fourth case, the time complexity for increasing values as well as decreasing and constant values will be the same as explained above. The only other situation is when the values increase after staying constant, or right after a sequence of decreasing numbers. In either case, we incur a cost of O(w)
// O(w)
// , as we clean up the deque using the pop() operation. If there is an increase in value after every w
// w
//  elements, we pay the O(w)
// O(w)
//  cost to clean up the deque. This can only happen \frac{n}{w}
// w
// n
// ​
 
//  times. So, the clean-up cost with such data will be O(n - (\frac{n}{w}) + ((\frac{n}{w})w))
// O(n−( 
// w
// n
// ​
//  )+(( 
// w
// n
// ​
//  )w))
// , that is, O(n)
// O(n)
// .

// Hence, the overall time complexity of the solution, irrespective of the input, is O(w+n)
// O(w+n)
// .

// Space complexity
// The space complexity of this solution is O(w)
// O(w)
// , where w
// w
//  is the window size.