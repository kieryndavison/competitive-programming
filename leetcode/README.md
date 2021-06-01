# LeetCode Notes
## 146. LRU cache
- Use doubly linked list and hash map
- Whenever you access or update an element, delete it in the linked list and move it to the front
- If the capacity of the cache is exceeded on a put action, then remove the last element in the linked list from the has map and linked list
## 75. Sort Colours
- Have 3 pointers, one for each colour, if loop while the middle pointer (for 1s) is less than  or equal to the last pointer (for 2s)
- Check the value at the middle pointer each time, if its a 0 then swap with the the 0 index pointer, if its 1 do nothing, if its 2 swap with the 2 index pointer
## Sort array of 0s and 1s
- Use two pointers, compare the elements at each pointer, if the element at the first pointer is less than the element at the second pointer then swap the elements at each pointer
- Increment the first pointer if the value of the index it is pointing to is a 0
- Increment the second pointer if the value of the index it is pointing to is a 1
## 545. Boundary of binary tree
- Use bfs with combination of preorder and post order traversal
- Preorder for left boundary, and post order for right
- Update the left and right flags as you go based on whether and left or a right node exists
    - ie. if we are going left but we don’t have any more left nodes then we want to set right to true and similarly on the other side
## 468. Validate IP address 
- First check if it is IP4 or IP6 potential by checking if it contains 3 dots or 7 colons
- Then check each segment of the IP address to validate it is a correct IP4 address or IP6 address
- If yes then return it otherwise return neither
## 526. Beautiful arrangement 
- Brute force, using recession and a loop try all possible values (1 to n) at all possible positions in the array
- Optimize by having a cache (memoization) to store the totals computed, with the key being the array and the value that you were trying to add to it
- Use a tuple for the array so that it can be used as a key
- In each iteration of the loop, if we can put the current element in the current position then recurse on the array with the element at that position remove (I.e. array[:j] + array[j+1:])
## 91. Decode ways
- Use dp 
- if the last element is valid (ie not equal to 0) then add its total to the current total I.e. prev1 or dp[I-1]
- If the string made using the second to last and last elements in the string is valid aka between 10 and 26 (inclusive) then add the second to last elements total to the current total (I.e. prev2 or dp[I-2])
- Return dp[n] or prev1
- Can optimize space complexity since only ever look at last or second to last element in dp - just use two previous trackers
## 56. Merge Intervals
- Sort 2d list by first element in second list, can just use sort or sorted for this, no need to specify parameter
- Go through arrays and update if the interval overlaps with the previous one
- Otherwise add the interval to the array
- Special cases - [[0,4], [1,3]] - ensure that when you merge intervals you are setting it to the max of the previous and current end time
- Intervals starting at 0, make sure that if you use a variable for the previous end time set it to float(‘-inf’)
    - Best to just check against the last element inserted directly, but must ensure that result array is not empty first
## 443. Compress string 
- Go through array, updating length of the current set of consecutive characters
- Keep track of the index that we would like to insert the next element into the array at as well 
- If the next character is not equal to the current character then add the current character to the array at the index we are keeping track of and increment that index
    - Then if the length of the number of consecutive characters was greater that 1, insert the length into the array character by character
    - Then reset the current length to 0
- In the end return the index that we would insert the next element to since this is equal to the length of the array
## 48. Rotate image
- Transpose and then reflect,
    - Transpose = reflecting elements across the diagonal - [I,j] = [j, I], starting nested loop from I, (optimization start from I+1 since all diagonal elements remain int eh same position)
    - Reflect = reverse each row, can do manually or use L[::-1] or L.reverse() to do it in place  
Get, set and setAll in o(1)
- Have a data structure with a ‘all’ variable and use a timestamp or just an increasing integer to determine whether to return the all value or the variable’s value 
## 3. Longest Substring without repeating characters
- Use an sliding window / two pointers and a map, keep track of the max length as we go
- All all characters in the string to a map as we get to them, with the key being the character and the index being the value
- If the current character is in the map and its last instance is within the sliding window then we want to update the max length and move the start of our window to be one after the last instance of the current character (so no repeats)
## 151. Reverse words in a string 
- Can do it in one line return “ ”.join(s.split()[::-1])
- Otherwise have to make to list to do it in place in python
- Steps:
    - Reverse entire string
    - go through array and reverse each word using 2 pointers and swapping when we see a space
    - Trim white spaces from front and back
    - Trim white spaces from middle
## 490. Maze
- Try each direction If it is not a wall or out of bounds
- Keep track of the elements we have visited 
- If we have already visited the current square, or is there are no more options return false
- If we reach the destination return true
## 953. Alien dictionary 
- Create a hash map with all the characters in the dictionary mapped to their position in the dictionary
- Go through all the characters of all the words in the dictionary and create a 2d array with all positions of all the characters in each word
- Compare each array of character positions with the one after it by iterating though zip(array, array[:1]) 
- If each word is less or equal to the next word then return true otherwise return false
- In python you can compare the arrays of positions directly to see if a word is less or equal to the next one in the list
## 1249. Minimum Remove to Make Valid Parentheses 
- Convert string to a list of 
- Go through the string, add the indexes of all the ‘(‘ to the stack
- If we find a ‘)’ remove its matching ‘(‘ from the top of the stack or else remove it from the list (I.e. set it to ‘’)
- After going through the string if we still have items in the stack, remove the characters at the indicies specified (i.e. set to ‘’)
## 1428. Leftmost column with at least a One
- Start from row = 0 and col = cols - 1
- Go through while row < rows and col >= 0
- If the value of the matrix at (row, col) == 0 then we go down since the row is sorted we know that there can be no more 1s in this row
- If the value of the matrix at (row, col) == 1 then we go left, since there may still be more 1s on the row
- In the end we return col + 1 since the final column index will be the rightmost column of all 0s
- If col + 1 == cols then there are no 1s in the matrix so we return -1
## 973. K Closest Points to the Origin:
- 2 possible methods, using a max heap or quick select 
- Max heap is O(NlogK), have to insert each item into a heap of size K, heap insertions cost log(size)
- Quick select is O(n) - at a maximum we go through each item twice
- Max heap algorithm: 
    - insert the negative of the distance to the origin for each point (since heap in python is a max heap)
    - If the heap size == k then pop the smallest element from the heap (since its - distance this will be the element farthest from the origin)
    - In the end return all the elements left in the heap
- Quick select algorithm:
    - 2 helper functions, one recursive, one partitioning 
    - if low < len(points) and high >= 0 then we partition the array
    - In the partition we select the last element as our pivot and keep track of the index  (i) where this pivot should go (starts at 0)
    - Go through the array and if an element in the array is less than the element at the pivot then swap it with the element at I and increment I
    - At the end we swap the pivot with the element at I and return I 
    - If I == k then we return since we have all elements <= k in the array[:k]
    - Otherwise if I < k then we want to find a greater index so we recurse on low = index+1
    - Otherwise I > k so we want to find a smaller index so we recurse on high = index - 1
## 680. Valid Palindrome 2
- Use normal 2 pointer palindrome solution, but if we find a mismatch, then we try removing either the left or right element s[left+1:right+1] and s[left:right]
- if either of those strings are palindromes (i.e. equal to its reverse) then we return true, otherwise we return false
- If we go through the entire string without mismatch we return true (as with the normal palindrome)
## 1570. Dot Product of Two Sparse vectors
- Use a List / array to store all the non zero elements in the vector and their indexes
    - Use list rather than a map since list is always O(1) to access a specific index, but map can be O(n) if there are a lot of elements inserted to it
- To calculate dot product have an index counter for both vectors non-zero lists and go through while both indexes have not reached the end of their respective list
- If the index value in the non-zero list at the current index is equal to the index value in the other non-zero list at the current index then we multiply the value of the vectors at that index and add it to the total and increment both index counters
- Otherwise we increment the index counter which corresponds to the smaller index value in the list
## 415. Add Strings
- Iterate through both strings in reverse using counters to keep track of the indexes
- If one counter reaches the end of its length then set the number to add to 0
- Keep track of a carry which is equal to the sum of the numbers and the carry divided by 10 (integer division - // in python)
- Add the sum mod 10 to a list which holds all the values computed
- After the loop add the carry to the list if its > 0
- Convert the list to a string and reverse it (has to be reversed since we were always adding to the back of the list)
## 238. Product of Array Except Self
- This is done in two passes first we calculate the product of all the elements that occur before each element in the array and then we multiply this by the product of all the elements that occur after each element in the array
- To calculate the product of all elements that occur before/after the given element in the array we keep a running product 
- At each iteration we multiply the element in the result array by this running product
- Then we multiply the running total by the current element in the array
## 560.Subarrat Sum Equals K
- Based on the idea that sum(i,j) = sum(0, j) - sum(0, i - 1)
- To compute this we have a dictionary which contains all the pre-sums aka sum(0, i - 1)
- Each time we go through the loop if sum(0, j) aka curSum - sum(i,j) aka k, is in the presum dictionary then we add the frequency of sum(0, i-1) to the res
- We have to add to the frequency since we can have negative numbers which means that we can have the same sum twice 
- Have to start with {0: 1} in the map for the case where curSum == k
## 270. Closeet Binary Search Tree Value
- Similar to normal binary search for target, except we keep track of the element that is the closest to the target and update it as we go
## 523. Continuous Subarray Sum
- Similar to other problems like this for example 560
- Main difference is since the subarray can add up to any multiple of k we use mod to optimize the solution
- We loop through the numbers in the array adding them to a prefix sum
- Each time we add to the prefix sum we also mod it by k so that the value stays between 0 and k
- If the prefix sum value has been seen before (i.e. is in the dictionary) and the index of the previous prefix sum is > 1 before the current index then we return true
- Otherwise we add the current prefix sum and the current index to the dictionary 
## 515. Find Largest Value In Each Tree Row
- Use either BFS or DFS
- BFS: 
    - keep track of all the elements in current row
    - While there is still non-null elements in a row 
    - Compute the max of the row and add it to the result list
    - And update the row to be the next row of non-null elements
- DFS:
    - Normal pre-order traversal but keep track of the level and update the result list
    - If the size of the result array is equal to the level (aka first element in a row) then add the element to the result list
    - Otherwise update the result list a the current level index to be the maximum of the current node’s values and its value
    - Recurse on the left and right trees, with level = level + 1
    - Return when node is None
## 139. Word Break
- 2 possible methods second is slightly optimized since we only consider substrings that have the length of words in the dictionary
- Method 1
    - Use dp, go through all possible final indices of the substring + 1 (i.e. 1… len(s))
    - Then for each i value go through from 0 … I-1
    - If dp[j] and s[j:i] is in the dictionary then set dp[I] to true (start with dp[0] = true) and break
    - Return dp[-1] 
- Method2 
    -  Similar to method 1 but instead for trying all possible substring for 0…I-1 for each I value we go through all words in the dictionary for each I value 
    - Since we are going through the words j = len(word)
    - Everything else is the same
## 67. Add Binary
- Basically the same as [415. Add Strings](## 415. Add Strings), only difference is we are working with base 2 rather than base 10 so we mod and divide by 2 rather than 10