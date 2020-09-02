test1 = "aabbbbbccdddeffg"
test2 = "racecar"
test3 = "iudefghillliipeidieid"

class pal:
    

    def __init__(self, newpal):
        self.bucket = dict()
        for c in enumerate(newpal):
            if c[1] not in self.bucket.keys():
                self.bucket[c[1]] = [c[0]]
            else:
                self.bucket[c[1]].append(c[0])
    
    def get_longest_palindrome(self, ):
        return None
    
    def get_bucket(self, ):
        return self.bucket

    def get_counts(self, ):
        self.counts = dict()
        for c in self.bucket.keys():
            self.counts[c] = len(self.bucket[c])
        return self.counts
            