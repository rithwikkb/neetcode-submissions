class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #[1,2,4,5]
        # first take the heaviest person(5)
        # after that, if the lightest person(left) is still less than remaining people, we keep on adding(whileloop)
        # this is optimal because we add the heaviest person first, and then lightest which makes sure its the minimum
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            remaining = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remaining >= people[l]:
                l += 1
        return res

        