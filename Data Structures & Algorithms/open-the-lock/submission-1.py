class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # thinking of the 8 states to remember 

        visited = set()
        dead = set()
        for d in deadends:
            dead.add(tuple(int(x) for x in d))
        if (0, 0, 0, 0) in dead:
            return -1
        target = tuple(int(t) for t in target)
        queue = []
        queue.append([0,0,0,0])
        visited.add((0, 0, 0, 0))
        count = 0 
        while queue:
            for _ in range(len(queue)):
                root = queue.pop(0)
                if tuple(root) == target:
                    return count 

                for i in range(4):
                    # for +1
                    new_state = root.copy()
                    new_state[i] = (new_state[i]+1)%10
                    if tuple(new_state) not in visited and tuple(new_state) not in dead:
                        visited.add(tuple(new_state))
                        queue.append(new_state)
                    
                    # for -1
                    new_state = root.copy()
                    new_state[i] = (new_state[i]-1)%10
                    if tuple(new_state) not in visited and tuple(new_state) not in dead:
                        visited.add(tuple(new_state))
                        queue.append(new_state)
                    

            count +=1
        return -1

