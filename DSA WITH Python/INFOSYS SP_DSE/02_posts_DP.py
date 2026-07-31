from functools import lru_cache
from bisect import bisect_right

def minimum_amplifiers(posts, r, K):
    n = len(posts)

    @lru_cache(None)
    def dp(i, super_left):

        if i >= n:
            return 0

        # Normal amplifier
        normal_end = posts[i] + 2 * r
        next_normal = bisect_right(posts, normal_end)

        ans = 1 + dp(next_normal, super_left)

        # Super amplifier
        if super_left > 0:
            super_end = posts[i] + 4 * r
            next_super = bisect_right(posts, super_end)

            ans = min(ans,
                      1 + dp(next_super, super_left - 1))

        return ans

    return dp(0, K)

posts = [1,3,5,7,10]
r = 2
K = 1
print(minimum_amplifiers(posts, r, K))