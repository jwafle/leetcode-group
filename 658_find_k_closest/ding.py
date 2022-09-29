class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        """naive solution: O(n)"""
        # queue to store result
        res = []
        
        # check if a is closer than b
        def closer(a, b):
            return (abs(a-x) < abs(b-x)) or ((abs(a-x) == abs(b-x)) and a <= b)
        
        # add to queue if not full
        # otherwise check if latest element is closer than start of the queue
        for item in arr:
            if len(res) < k:
                res.append(item)
            else:
                if closer(item, res[0]):
                    res.pop(0)
                    res.append(item)
                else:
                    return res
        return res

        """binary search: O(logN + k):
        sorted already so we just need to find the slice of 
        the arr to return. Only need to shift start and end of slice
        no need to iter through all elements"""