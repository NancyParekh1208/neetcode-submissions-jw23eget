class MedianFinder:

    def __init__(self):

        self.res = []
        

    def addNum(self, num: int) -> None:
        self.res.append(num)
        

    def findMedian(self) -> float:
        self.res.sort()
        if len(self.res)%2 == 0:
            return (self.res[len(self.res)//2] + self.res[(len(self.res)//2) -1])/2
        return self.res[len(self.res)//2]

        
        