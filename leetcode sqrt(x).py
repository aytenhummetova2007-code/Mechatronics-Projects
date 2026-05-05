class Solution:
    def mySqrt(self, x: int) -> int:
        sol, sag = 0, x
        while sol <= sag:
            orta = (sol + sag) // 2
            if orta * orta <= x:
                sol = orta + 1
            else:
                sag = orta - 1
        return sag