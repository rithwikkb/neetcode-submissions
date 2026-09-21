class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            # if any of the corresponding values in the triplet are greeater than that of the target, it means it can never match since we take the max, so we can skip the triplet as a whole
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # now we can go over each individual triplet and check if the number matches that of the target, if so, we can add the value to the set
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        # since its a set,the values will be unique so it should be equal to the target if we make target a set
        return len(good) == 3
        