class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr = 0
        p2 = len(s)- 1        

        s = s.lower()

        if(len(s) == 0 or len(s)==1):
            return True

        while(p2>=ptr):

            while(p2 >= 0 and not s[p2].isalnum()):
                p2-=1
            while(ptr < len(s) and not s[ptr].isalnum()):
                ptr+=1            

            if(ptr>=p2):
                return True
            if (s[ptr] != s[p2]):
                return False
            
            
            p2-=1
            ptr+=1

        return True
        