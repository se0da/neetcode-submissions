class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = [st for st in s if st.isalnum() or st.isspace()]
        clean_string = "".join(clean_string)
        if(clean_string.replace(" ", "").lower() == clean_string.lower().replace(" ", "")[::-1]):
            return True
        else:
            return False