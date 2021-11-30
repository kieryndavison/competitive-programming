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
## 560. Subarray Sum Equals K
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
    - If dp[j] and s[j:i] is in the dictionary then set dp[i] to true (start with dp[0] = true) and break
    - Return dp[-1] 
- Method2 
    -  Similar to method 1 but instead for trying all possible substring for 0…I-1 for each I value we go through all words in the dictionary for each I value 
    - Since we are going through the words j = len(word)
    - Everything else is the same
## 67. Add Binary
- Basically the same as [415. Add Strings](#415-Add-Strings), only difference is we are working with base 2 rather than base 10 so we mod and divide by 2 rather than 10
## 314. Binary Tree Vertical Order Traversal 
- The main idea for this algorithm is to use BFS and store both the node and the colum value for each node in the tree
- We also keep track of the minimum and maximum column value that we have seen so far as an optimization so we dont have to sort the lists of values at the end based on their column value
- We keep store all the values in the tree in a dictionary with the key being the column value and value being the list of node values at that column index
## 528. Random Pick with Weight
- In the init function we create and store a prefix array for each index
- In the pick index function we generate a random number between 1 and the total sum of all the weights (i.e. prefixSum[-1]) and then binary search for that value in the array
- In the end we return low
## 1762. Buildings With an Ocean View 
- Simple O(n) solution, just iterate through the array in reverse and keep track of the tallest building you have seen so far
## 426. Convert Binary Search Tree to Sorted Doubly Linked List
- Use a typical in order traversal, but keep track of the previous and head nodes
- If the previous node is None then we have found the head node so update the head value to point to the current node
- Otherwise update the left node of the current node to be the previous node and the right node of the previous node to be the current node 
- Then update the previous node to be the current node
- After the recursion is complete then close the loop by updating the left pointer for the head node the point to the last node (i.e. the current previous) and update the right pointer for the previous to be the head node
- Then return the head node
## 605. Can place flowers
- For each element in the array:
    - If it is a 0 check if the one directly to its right and left is also 0 (if they exist)
    - If it is set the current element to 1 and update the number of flowers counter 
    - Then if the counter is greater than the number of flowers we want to plant (n) then return true
- If we go through the entire loop without returning then return false
- Edge case: first and last elements, for the first one only check the right side and for the last only check the left
## 31. Next Permuation
- Three step algorithm
- First find the first element that is smaller than the one that comes before it, lets call it element a
- Then find the first element that comes before element a that is smaller than it, say element b, then swap element a with elment b
- Finally, reverse the number from the one after the original index of element a to the end 
## 200. Number of Islands
- For each element in the array, if it is a 1 then increment the island counter by 1 and dfs on the array from the element to set all 1s in the island to 0 / #
- In the dfs we recurse on up, down, left and right elements in the 2d array setting each element to 0 / # and return when we find a element that is not 1 or reach the bounds of the 2d array
## 582. Kill Process
- Prerocess the arrays and make a dictionary that maps each process to its direct children
- Then preform a dfs starting from the process to kill and at each iteration add the popped element to the result and then add all its children to the queue
## 1283. Find the smallest divisor given a threshold
- Use binary search, low = 1, high = max of the numbers in the array
- In each iteration 
    - Calculate the sum for the mid point, by adding the ceiling of each element divided by the divisor to the sum
    - Can take the ceiling by doing (num + divisor - 1) // divisor
    - If the sum is greater than the threshold then we want a larger divisor so we set low = mid + 1
    - Otherwise we want a smaller divisor so we set high = mid - 1
- In the end we return low
## 1419. Minumum Number of Frogs Croaking
- Use a state machine
- Represent state machine as dictionary where each character is mapped to the number of times it occured, or the number of croaks that are currently on that letter
- To avoid repeated code also create a map which maps each character to the one that should come before it
- In each iteration 
    - Update the the map at the current letter
    - If the character is a c then update the counter for the number of frogs that are currents croaking and the max
    - If the count of the previous letter is 0 the return -1 since the letters are out of order
    - Otherwise update the count of the previous letter
    - If we are at the last letter in the word then update the counter for the number of frogs that are currently croaking
- In the end if there are no frogs currently croaking then return the max
## 696. Count Binary Substrings
- 2 main parts: 
    - First we must compute the length of each group of 1s or 0s
    - Then we calculate the number of substrings we can produce by taking the minimum of the length of the current substring and the previous
- Version 1:
    - Can do this in one pass by keeping previous, and current counters
    - If the current character is equal to the previous one then we increment the current counter
    - Otherwise, we add to the result the minimum of the previous and current group lengths and set current back to 1 and previous to current
    - In the end we also have to add the min of the previous and current groups to the result to account for the last groups in the string
- Version 2:
    - Add in spaces between all the groups 0s and 1s and then split the string on the spaces and calculate the len of each group
    - Then go through the array of the group lengths and the array without the first element (using zip) and take the minimum of the first and second array values and add it to the running sum
    - return the running sum at the end
    - This used O(n) space and 2 passes but it uses more of pythons built in functionality 
## 243. Shortest Word Distance
- Keep track of the most recent index of each word in the list
- If both words have been seen then update the minimum distance to be the minimum of its current value and the current distance between the two words
- Return the minimum distance variable in the end
## 225. Implement Stack Using Queues
- Make push O(n) since both pop and top require the queue to be in reverse order
- Each time an element is added to the queue then pop and append all elements again
- All other methods are trivial
- Only requires 1 queue, since we pop and append to the same queue again
## 496. Next Greater Element I
- Preprocess the second array first to optimize the solution
- Use a stack and dictionary to store each value and its next greater element:
    - Push all elements on the stack 
    - While the element is greater than the element on the top of the stack pop elements from the stack and add the popped element to the dictionary with a value of the current element
- Then go through the first array and add the value for each number to the result array
- Return the result array
## 1309. Minimum Difference Betweet Largest and Smallest Value in Three Moves
- We know that if there are less than 5 elements in the array then the difference is 0 since we can set all elments to the same value in 3 moves.
- Otherwise, there are 4 options to consider: 
1. Removing largest 3 elements
2. Removing smallest element and largest 2 elements
3. Removing smallest 2 elements and largest element
4. Removing smallest 3 elements
- For each case the difference between the largest and smallest values in the array is:
1. The 4th largest elment - the smallest element 
2. The 3rd largest element - 2nd smallest element
3. The 2nd largest element - 3rd smallest element
4. The largest element - 4th smallest element
- So we need to find the 4 largest and 4 smallest elements and then subtract them from eachother to find the minimum difference.
## 1048. Longest String Chain
- DP solution
- Sort array of words by length
- Go through the sorted array and for each word try removing each character to create a word2
- The length of the chain = length(word) = max(length(word), length(word2) + 1)
## 735. Asteroid Collision
- There will be a collision if there is a positive integer to the left of a negative integer
- Keep a stack of all the values seen so far
- While the current value is negative and the value at the top of the stack is positive 
    - If the negative of the current value is greater than the value on the top of the stack then pop from the stack
    - If the negative of the current value equals the value at the top of the stack then pop from the stack and break from the loop
    - If the negative of the current value is less than the value at the top of the stack then break from the loop
- Otherwise add the current value to the stack
## 1277. Count Square Submatrices with All Ones
- Use dp
- If the cell has value 1 then the number of square submatrices that can be made using all the cells up to that point is equal to the min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
- If i == 0 or j == 0 and the cell have value 1 then the number of square submatrices that can be made is equal to 1
- The total number of square submatrices that can be made is equal to the sum of the values computed for each cell in the array
## 1525. Number of Good Ways to Split a String
- Use collections.Counter to create a dictionary mapping each character in the string to how many times it occurs
- Go through each character in the string and add it to the left side dictionary and remove it from the right side dictionary
- If the dictionary value at the current character in the right side is 0 then remove it from the dictionary
- If the length of the left and right dictionary is equal then we have found a split that works since we want the number of distict characters to be the same.
## 690. Employee Importance
- Make a dictionary mapping employee id to employee properties
- Perform dfs on the list of employees, starting from the id given
- return the sum of the employee importance and all their subordinates importances.
## 833. Find And Replace in String
- Key: go through the string in reverse that that you don't have to keep track of the change in indicies 
- As you go if the source is equal to the string at that index then replace with the target, otherwise leave the string as is
## 394. Decode String
- Use a stack or recursion 
- There are 4 cases:
1. When you find an opening bracket '[' then recurse, or push to the current sting and multiplier on to the stack
2. When you find a closing bracket ']' then return or compute the current string (string from the top of the stack + current string times the number from the top of the stack)
3. When you find a number add it to the current multiplier (multiplier * 10 + int(char))
4. When you find a letter add it to the current string
## 42. Trapping Rain Water
- Use two pointers, and keep track of the left and right max
- At each iteration of the loop increment the pointer on for whichever side has a lower height, recompute the max for that side and add the difference between the max and the current height to the result 
- Intuitively, since we are always moving the smaller of the two pointers, there will be a larger bar in the other side (i.e. right). Therfore, we know that the amount of water trapped only depends on the max in the current side (i.e. left).
## 422. Valid Word Square
- Straight forward solution, go through the list of words and then go through each character in each word (i.e. character at i, j) and check if it is equal to the character at j, i.
- If we find a case where the characters are not equal then it is not a square so return false
- Otherwise return if we complete the loop return true
- Two edge cases - the index j is larger than the length of the list or the index i is larger than the length of the word at j
## 425. Word Squares
- Use a trie - store all prefixes and the words in a dictionary with the prefix as the key and the words as the value (note words can be a set) 
- Recursively go through all the words an try to create a square with them
- Note in the prefix trie all words map to "", therfore starting at index 0 with square = [] will recursively try to create squares with all the words
- Base case: when a square has length n = length of the word
- Find the prefix for the current square based on the words in the square and then recursively try adding each word with this prefix to the trie
## 281. Zigzag Iterator
- Use a queue to store the next value to be returned and its iterator
- hasNext() checks if the queue is empty
- next() pops an element from the queue, returns the value poped and re-adds the iterator to the queue
- In the _insert_in_queue function we try to insert the iterator and its next value into the queue, if an StopIteration exceptions is thrown then we do nothing and the value will not be added to the queue
## 529. Minesweeper
- Basic DFS/BFS solution, two cases:
1. If we click a mine then set it to X and return immediately
2. Otherwise recurse until you find a square that has mines adjacent to it. In each iteration determine the number of adjacent mines, if there is any then set the square the the number of adjacent mines and return. Otherwise set the square to 'B' and recurse on all adjacent squares.
## 575. Distribute Candies
- Key: use a set to determine the number of candy types
- Take the min of the length of the set of candy types and the length of the candy types array divided by 2
## 300. Longest Increasing Subsequence
- Intuition: Keep track of the smallest numbers that can go in each position of the subsequence, since you want to know the longest increasing subsequence. The smaller the value the more likely other values will be greater than it
- Store these values in an array
- For each element binary search in the array of the smallest numbers and update the value at the index returned to be the current element
    - This will either update an element in the array to be a smaller value or add a new value to the end of the array.
## 289. Game of Life
- Key: use 2 bits, in the first bit store the new value and in the previous bit store the current value. 
- To start we have dead => 00 and alive => 01, after setting the values there are 4 possible options: 00 (new and current values are dead), 01 (new value is dead, current value is alive), 10 (new value is alive, current value is dead), 11 (new and current values are alive)
- To get the current value use board[i][j] & 1 - gets the second bit
- To get the new value use board[i][j] >> 1 - gets the first bit (can also use board[i][j] & 2)
## 322. Coin Change
- Use dp - only need to store 1-d array
- Initialize it to 0 and then the rest infinite 
- Go through 0 - amount and all coin options
    - If i >= coin then set the value to be min(dp[i-coin] + 1, dp[i])
    - dp[i] contains how many coins are needed to make i with the current coin options
## 843. Guess the Word
- Main idea: eliminate any words that do not have the same number of matches as the current word and the secrete word. To do this, at each iteration, go through all the words in the wordlist and only keep the words where the sum of equal characters between the word and the guessed word (guess) is equal to the result of Master.guess(guess).
- Optimization: consider what value initally guess. For this we want to take the word that overlaps with the most other words in the list. This is because this word is most likely to overlap with the secrete word which helps to narrow down the word list faster. To find the word with the most overlap with other words we find the word with the largest score, where score is equal to the sum of the number of times each character in the word occurs at that position accross all words in the word list. We use a list of dictionaries to store this, where the index in the list repesents the position the character occurs in the word and the dictionary specifies how many times each character occurs at that position.
## 1293. Shortest Path in a Grid with Obstacles Elimination
- Main idea: Use BFS storing the current row, col, number of obstacles in the path and length of the path. Keep track of the cells visited in a set (slight optimization to list) and return the length when you get to cell n - 1 and m - 1.
- Optimization: if k is large enough then we can directly go down and right removing all obstacles in the way. Since we know that the last cell will never has an obstacle if k >= n + m - 3 then shortest path = n + m - 2
## 1610. Maximum Number of Visible Points
- Compute the polar angles for all the points. To do so use math.atan2(y2-y1, x2-x1). Make sure count the number of points that are the same as the location so that they can be added to the result at the end since they are included in any field of view.
- After computing all the polar angles, sort them and then add each angle * 2pi to the array so points in the 1st quadrant can be included in fields of view starting the the 4th quadrant. Also make sure to convert the angle given to radians so that it will be compared properly to the angles computed from the points.
- Finally, use 2 pointers to determine the max number of points that can be contained in a field of view. Start with start and end = 0, go through each element in the array and update start to ensure that angles[end] - angles[start] <= angle (use while loop inside for loop). Update the result at each iteration to be the difference between the start and end index + 1
- Return the result + the number of points that are the same as the location point
## 68. Text Justification
- Not much tricks here just go through the array of words and keep track of the words and how many characters are in the current line.
- Once you find that adding the current word would exceed the maxWidth for a line create a line and add it to the result
- In order to correctly distribute spaces we can use a round robbin method where we go through each value from 0 to the number of spaces we need to insert to get length of the line = maxWidth (aka maxWidth - number of characters in the line). We add the space to the word at index i % the number of places we have to insert spaces in. This ensures that the spaces are evenly distributed and any extra spaces are added to the leftmost slots.
- After the outer loop we add the last line to the result and left justify it.
## 981. Time Based Key-Value Store
- Use a hashmap to store the key and a list of pairs (timestamp, value)
- When a get request is made we binary search on the list of pairs and return the value of the pair with the largest timestamp that is less than or equal to the current timestamp
- We can use binary search directly with out sorting the list since we know that the timestamps for a specific key will always be given in ascending order
## 871. Minimum Number of Refueling Stops
- Two possible solutons: dp or using a priority queue.
- For DP solution we store the maximum distance we can travel with i stops at dp[i]
- We compute dp[i+1] by going through all the stations and then going through the dp array in reverse from i to 0 and if the value of dp[i]>= to the current distance then update the value of dp[i+1] to be the max of dp[i+1] and the dp[i] + the amount of fuel at the current station. Go through the array in reverse since we are updating the value at i+1.
- Time complexity = O(n^2), space complexity = O(n), where n is the number of stations.
- For priority queue solution we use a priority queue to store the amount of fuel at all the stations we have passed so far but not used, we also keep track of the current fuel level, the previous distance we were at and the number of stops we have made.
- Go through each station and subtract the distance between the current station and the previous station from the current fuel level.
- If the current fuel level is less than 0 then we know we would have had to refuel at, at least one of the previous stations. The optimial station to choose is the one with the most fuel since it will take us the closest to the destination. Since we are using a priority queue to store the amount of fuel at the previous stations we can simply pop an element from the priority queue and add the amount of fuel to the current fuel level. 
- Continue popping elements from the pq until the fuel level becomes greater than 0 or the pq is empty.
- If the fuel level is still 0 after this then we know that we cannot reach the destination so we return -1.
- Otherwise we add the negative of the current stations fuel to the pq and set prev to be the current distance.
- Note: we add the negative of the fuel values to the pq since it is a min heap and we want the largest fuel values to be popped first.
- Time complexity = O(nlogn), space complexity = O(n), where n is the number of stations.
## 465. Optimal Account Balancing
- First calculate the balance for each person by adding their total if they receive money and subtracting their total if they give money.
- Then convert the dictionary storing everyone's balance to a list of all the balances with balance != 0, called debt.
- DFS on debt starting from index 0.
- Find the first element with balance != 0
- If there are no elements with balance != 0 then we know that everyone all debt has been settled and we return 0.
- Otherwise go through all the values starting from index + 1 and if the value at debt[j] has opposite sign to the value at debt[index] then set d[j] += d[index] and recurse on index + 1.
- After the recursion we backtrack and set d[j] -= d[index] so that we can use d[j] in a different combination of transactions.
- Time complexity = O(n!), since we have to brute force try every combination, space complexity = O(n), since both the balances map and debt array have length n, where n is the number of people.
## 410. Split Array Largest Sum
- We can use binary search and a greedy approach to solve this problem.
- We know that the largest sum among the m subarrays must be between the max value in the array and the sum of all the elements in the array. This is because the max value must be included in one of the subarrays and in the case where m = 1 we will include all values in one subarray.
- With these constraints defined we can simply binary search with low = max(nums) and high = sum(nums).
- At each iteration of the binary search we split the array into subarrays with sum <= mid. If the array is split into <= m subarrays then we know that the largest sum is <= mid, so we set high to mid.
- Otherwise if there are > m subarrays then we know that the largest sum is > mid, so we set low to mid + 1.
- In the end we return low but we could also return high since they are loop ends when they are the same value.
- Time complexity = O(nlog(sum(array))), space complexity = O(1)
## 1146. Snapshot Array
- Basic approach store an array or arrays and each time we snapshot the array we copy the last array in the array of arrays and add it to the end.
- However, we can optimize this approach to only add values if they are updated. Now we will have an array of pairs where the first element is the snapshot_id and the second element is the value of the array at that snapshot.
- In get we binary search for the closest snapshot_id at array[index] that is less than or equal to the snapshot_id requested. 
- Time complexity = O(log(s) + n), space complexity = O(s), where s is the number of times snap() is called and n is the length of the array.
## 1110. Delete Nodes And Return Forest
- Fairly straight forward recursive approach. Go through and keep track of whether each node is a root. If it is a root and it is not deleted then we add it to the result. Then we recurse on the left and right children and update the left and right children based on the result of that recursion. Then we return None if the node was deleted and otherwise we return the node. Base case: if the current node is None then we return None. 
- Runtime complexity = O(n), where n is the number of nodes in the tree, Space complexity = O(n + h), where h is the height of the tree.
## 366. Find Leaves of Binary Tree
- Simple recusive approach. Depends on height of a node = max(height of left child, height of right child) + 1. Use recursion to determine the height of each node and then insert the node into the result at its height. For example leaf nodes have height 0, so we insert them at index 0. Base case, if the node is None then return -1 since there is no height.
- Runtime complexity = O(n), Space complexity = O(n), where n is the number of nodes in the tree.
## 1937. Maximum Number of Points with Cost
- Use a version of dp where we keep track of the max points from the left and right of the current index.
- For each row we compute the max points from the left and right, where left[j] = max(left[j-1] - 1, points[i][j]) and right[j] = max(right[j+1] - 1, points[i][j]). Then we update the dp[i+1][j] to be points[i+1][j] + max(left[j], right[j]) where left and right are the max points from the left and right of the current index.
- Optimization #1: Since the input (points) is already a 2d array we can use it to store our dp array. Although this does not reduce our space complexity it removes the need to copy the cur array into the pre array at each iteration of the outer loop and copying is generally expensive.
- Optimization #2: We can actually reduce the space complexity to O(1) and have one less iteration of the elements in a row by updating dp[i+1][j] to be dp[i+1][j] + dp[i][j] in the loop to determine the left values. To do this we first loop through in reverse and update dp[i][j] to be the max(dp[i][j], dp[i][j+1] - 1) (aka computing the right values). Then we loop through and update dp[i][j] to be the max(dp[i][j], dp[i][j-1] - 1). Now we know that dp[i][j] is the max points from the left and right so we can directly set dp[i+1][j] += dp[i][j].
- With no optimizations and optimization #1 we have Time complexity = O(n^2), Space complexity = O(m), where n is the number of points and m is the number of points in a row.
- With optimization #2 we have Time complexity = O(n^2), Space complexity = O(1).
## 2007. Find Original Array From Doubled Array
- In python we can directly convert the array to a hashmap mapping each value to the number of times it appears using the collections.Counter() function.
- We the loop through the map in sorted order and subtract the number of times each value appears from value * 2. Going through the loop in sorted order ensures that we only have to look for values with value * 2 not value / 2. In the case wher value == 0 then we subtract the number of times it occurs / 2 since 2 * 0 = 0.
- If the number of times a value appears is more than the number of times value * 2 appears then we know that the array is not doubled so we return [].
- In the end we return any values in the map which have a value > 0. We can use list(val.elements()) to get all numbers with val > 0.
- Time complexity = O(n + klog(k)), Space complexity = O(n), where n is the number of elements in the array and k is the number of unique elements.
