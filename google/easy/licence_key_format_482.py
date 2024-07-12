from typing import Deque
from collections import deque

class LicenceKeyFormat:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        queue: Deque = deque()
        count: int = 0
        for el in s[::-1]:
            if el != "-":
                if count > 0 and count % k == 0:
                    count += 1
                    queue.appendleft("-")
                    queue.appendleft(el.upper())
                else:
                    count += 1
                    queue.appendleft(el.upper())
        return "".join(queue)