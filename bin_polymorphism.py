
class Students():

    def __init__(self, sid, sname, scores):
        self.sid = sid
        self.sname = sname
        self.scores = scores

    def __str__(self):
        return (f'Student name: {self.sname} \t ID: {self.sid} \t scores: {self.scores}')

    def __eq__(self, other):
        if self.sname == other.sname:
            return True
        else:
            return False

    def binsearch(self, left, right, target):
        if left <= right:
            mid = (left+right) // 2
            if self.scores[mid] == target:
                return mid
            elif self.scores[mid] < target:
                left = mid + 1
                return self.binsearch(left, right, target)
            else:
                right = mid - 1
                return self.binsearch(left, right, target)
        else:
            return -1


class Numbers():
    def __init__(self, nid, scores):
        self.nid = nid
        self.scores = scores

    def __str__(self):
        return (f'Numbers id: {self.nid} \t {self.scores}')

    def __eq__(self, other):
        if self.nid == other.nid:
            return True
        else:
            return False

    def binsearch(self, left, right, target):
        if left <= right:
            mid = (left+right) // 2
            if self.scores[mid] == target:
                return mid
            elif self.scores[mid] < target:
                left = mid + 1
                return self.binsearch(left, right, target)
            else:
                right = mid - 1
                return self.binsearch(left, right, target)
        else:
            return -1


s1 = Students(100, 'John', [100, 100, 100])
s2 = Students(101, 'James', [70, 80, 90, 100])
print(f'{s1}\n{s2}')
ret = s2.binsearch(0, len(s2.scores)-1, 90)
print(ret)

n1 = Numbers(101, [90, 91, 93, 95, 100])
n2 = Numbers(102, [100, 110, 130, 140, 105])
print(f'{n1}\n{n2}')

ret = n1.binsearch(0, len(n1.scores)-1, 100)
print(ret)

target = 100
for p in (s1, s2, n1, n2):
    ret = p.binsearch(0, len(p.scores)-1, target)
    print(f'Found the taget value at the index {ret}')
