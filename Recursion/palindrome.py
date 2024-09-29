
class SP:
    def check_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s, start=0, curr=None, res=None):
        if res is None:
            res = []
        if curr is None:
            curr = []
        if start == len(s):
            res.append(curr[:])
            return res

        for i in range(start, len(s)):
            if self.check_palindrome(s[start:i+1]):
                curr.append(s[start:i+1])
                self.partition(s, i+1, curr, res)
                curr.pop()
        return res

    def main(self):
        s = "SANDHYA"
        partitions = self.partition(s)
        for part in partitions:
            print(part)

# Creating an instance of SP class
gfg_obj = SP()
gfg_obj.main()