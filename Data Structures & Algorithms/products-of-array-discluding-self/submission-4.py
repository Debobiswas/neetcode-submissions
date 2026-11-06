class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1=0
        p2=len(nums)-1

        pref=[]
        suf=[]

        
        while(p1 < len(nums)):
            if (p1 == 0) :
                pref.append(nums[p1])
                suf.append(nums[p2])
                p1+=1
                p2-=1
            else:
                pref.append(nums[p1]*pref[p1-1])
                suf.append(nums[p2]*suf[p1-1])
                p1+=1
                p2-=1
        suf.reverse()

        res = []
        i=0
        while i < len(nums):
            if(i==len(nums)-1):
                res.append(pref[i-1])
                i+=1            
            
            elif(i==0):
                res.append(suf[i+1])
                i+=1

            else:
                res.append(pref[i-1]*suf[i+1])
                i+=1

        return res
