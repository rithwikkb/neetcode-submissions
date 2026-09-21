class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        # 4 cases. 1 is if the customer gives a 5, then you add it to fives. if the customer gives a 10, you must take the 10 and give the 5. if its a 20 and you have a ten, then you give 1 ten 1 five. if not, you give 3 fives
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                fives -= 1
                tens += 1
            elif i == 20 and tens > 0:
                fives -= 1
                tens -= 1
            else:
                fives -= 3
            if fives < 0:
                return False
        return True

        