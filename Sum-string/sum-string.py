class Solution:
    def isSumString(self, S):
        n = len(S)

        def sum_strings(a, b):
            ans = ""
            a, b = a[::-1], b[::-1]
            carry = 0
            index = 0

            while index < len(a) and index < len(b):
                s = int(a[index]) + int(b[index]) + carry
                carry = s // 10
                s %= 10

                ans += str(s)
                index += 1

            while index < len(a):
                s = int(a[index]) + carry
                carry = s // 10
                s %= 10

                ans += str(s)
                index += 1

            while index < len(b):
                s = int(b[index]) + carry
                carry = s // 10
                s %= 10

                ans += str(s)
                index += 1

            if carry:
                ans += str(carry)

            ans = ans[::-1]

            return ans

        def helper(a, b, p, valid):
            if p == n:
                return valid

            need = sum_strings(a, b)
            cur = ""

            i = p
            while i < n:
                cur += S[i]

                if cur == need:
                    return helper(b, cur, i + 1, True)
                i += 1

            return False

        for i in range(1, n + 1):  # length of the first string
            for j in range(i + 1, n + 1):  # second string will end at j - 1
                a = S[:i]
                b = S[i:j]

                if helper(a, b, j, False):
                    return 1

        return 0