class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):

            # Expand the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Shrink until the window is valid
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            # Update max length AFTER shrinking
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length