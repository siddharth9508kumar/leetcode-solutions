class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [[]]
        groups = [[]]
        
        for char in expression:
            if char == '{':
                stack.append(groups)
                groups = [[]]
            elif char == '}':
                # Evaluate union inside the braces
                union_set = set(word for group in groups for word in group)
                groups = stack.pop()
                # Concatenate with the preceding expression in the current product group
                if not groups[-1]:
                    groups[-1] = list(union_set)
                else:
                    groups[-1] = [a + b for a in groups[-1] for b in union_set]
            elif char == ',':
                # Union operator: start a new product group
                groups.append([])
            else:
                # Concatenation of a literal character
                if not groups[-1]:
                    groups[-1] = [char]
                else:
                    groups[-1] = [a + char for a in groups[-1]]
                    
        res = set(word for group in groups for word in group)
        # to give the unique values only sort the res
        return sorted(list(res))