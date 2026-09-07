class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for aster in asteroids:
            # A collision can only occur if the current asteroid is moving left (< 0)
            # and the asteroid at the top of the stack is moving right (> 0)
            while stack and aster < 0 < stack[-1]:
                # Top asteroid is smaller; it explodes, so pop it and check again
                if stack[-1] < -aster:
                    stack.pop()
                    continue
                # Both asteroids are equal in size; both explode
                elif stack[-1] == -aster:
                    stack.pop()
                # Current asteroid is smaller; it explodes (break out without pushing)
                break
            else:
                # Executes if no collision occurs, or if current asteroid destroyed all right-moving ones
                stack.append(aster)
                
        return stack