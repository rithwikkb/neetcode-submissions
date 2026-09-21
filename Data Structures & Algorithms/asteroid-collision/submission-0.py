class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            # we check if the current asteroid is less than 0 and if the top of the stack is greater than 0(coz they collide)
            while stack and i < 0 and stack[-1] > 0:
                # we get the difference
                difference = i + stack[-1]
                # if difference is less than 0 that means the curr asteroid is bigger, so we pop the top one from the stack
                if difference < 0:
                    stack.pop()
                elif difference > 0: # if it is greater than 0 then the top is greater, so we just discard the curr asteroid by setting it to 0
                    i = 0
                else: # if they are equal we do both, we remove the top and discard the curr asteroid
                    i = 0
                    stack.pop()
            if i: # now if the curr asteroid still exists after the checks, we append to stack
                stack.append(i)
        return stack