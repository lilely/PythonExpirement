class Solution:
    def findKLargest(self,array,k):
        if array.count < k:
            return None
        cursor = array[0]
        pos = self.partion(array, cursor)
        print(array)
        print(pos)
        if pos+1 == k:
            return array[pos]
        elif pos+1 < k:
            slice = array[pos+1:]
            return self.findKLargest(slice,k-pos-1)
        else:
            slice = array[:pos]
            return self.findKLargest(slice,k)


    def partion(self,array,cursor):
        i = 0
        j = len(array) - 1
        while(i != j):
            while array[j]<cursor:
                j -= 1 
            while array[i]>cursor:
                i += 1
            array[i],array[j] = array[j],array[i]
            # print("i = {}".format(i))
            # print("j = {}".format(j))
            # print("===========")
        return j

print(Solution().findKLargest([3,1,2,5,6,7,8,4,9],3))