class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start_index, current_sum, path):
            # Base case: If the current sum equals the target, add the current path to the result
            if current_sum == target:
                result.append(path)
                return
            # If the current sum exceeds the target or we've reached the end of candidates, return
            if current_sum > target or start_index == len(candidates):
                return
            
            # Continue exploring combinations, starting from start_index
            for i in range(start_index, len(candidates)):
                # Avoid duplicate combinations by skipping candidates that are the same as the previous candidate
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                # Include the current candidate in the path
                backtrack(i + 1, current_sum + candidates[i], path + [candidates[i]])
        
        result = []  # List to store the result
        candidates.sort()  # Sort the candidates to handle duplicates
        backtrack(0, 0, [])  # Start backtracking from the beginning with current_sum = 0 and an empty path
        return result
