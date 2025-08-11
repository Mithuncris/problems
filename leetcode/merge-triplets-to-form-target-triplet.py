class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        good = set()
        for x, y, z in triplets:
            if x<=target[0] and y<=target[1] and z<=target[2]:
                good.add((x,y,z))
        xx = yy = zz = False
        for x,y,z in good:
            if x==target[0]:
                xx = True
            if y==target[1]:
                yy = True
            if z==target[2]:
                zz = True
        return xx and yy and zz