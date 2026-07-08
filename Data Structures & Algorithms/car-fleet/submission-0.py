class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ss = sorted(zip(position,speed))
        s = []

        for i,j in reversed(ss):
            time = (target - i) / j

            if len(s) == 0 or time >  s[-1]:
                s.append(time)

        return len(s)


        