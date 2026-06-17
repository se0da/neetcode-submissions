class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # Quick check if s1 is longer than s2
            return False
        
        s1_map, s2_map = {}, {}
        
        # Build the frequency map for s1
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        # Initialize the frequency map for the first window in s2
        for i in range(len(s1)):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        
        # Compare the maps for the first window
        if s1_map == s2_map:
            return True
        
        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character to the window
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            
            # Remove the character that is no longer in the window
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:  # Clean up the map to avoid zero entries
                del s2_map[s2[l]]
            l += 1  # Move the left pointer
            
            # Compare the maps
            if s1_map == s2_map:
                return True
        
        return False
