class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
          s += i + "wtf"
        return s

    def decode(self, s: str) -> List[str]:
        lis = s.split("wtf")
        return lis[:-1]