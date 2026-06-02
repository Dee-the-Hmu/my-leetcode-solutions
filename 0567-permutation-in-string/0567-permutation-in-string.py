"""
U: 
    input: 2 strings "s1" and "s2" 
    output: boolean 
M: 2 dict 
P: 
    1. create a dict, org_d, key = char in s1 and value = its count, update_needed = False
    2. create another dict, curr_d = org_d.copy()
    create right pointer = 0, left ptr = 0 
    3. iterate s2, for each char #right pointer 
        char = s[right]
        4. if char in curr_d: 
                while char in curr_d: 
                char = s[right]
                5. curr_d[char] -= 1 
                    update_needed = True
                6. if curr_d[char] == 0 
                    7. del curr_d[char]
                right += 1
                7. if not curr_d:
                    return True 
            else: #not in d 
                left += 1
                right = left
                continue 
        right += 1
        8. if update_needed: 
            curr_d = org_d.copy()
            update_needed = False

    return False 
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        org_d = {}
        d = {}
        update_needed = False
        right = 0
        left = 0

        for char in s1: 
            org_d[char] = org_d.get(char, 0) + 1 

        d = org_d.copy()

        while left <= right and right < len(s2):
            char = s2[right]

            if char in d: 
                while right < len(s2) and char in d: 
                    d[char] -= 1 
                    update_needed = True 
                    if d[char] == 0:
                        del d[char]
                    
                    if not d: 
                        return True
                    right += 1 
                    if right < len(s2):
                        char = s2[right]
            
            else: 
                left += 1
                right = left 
                if update_needed: 
                    d = org_d.copy()
                    update_needed = False

        return False
            

        