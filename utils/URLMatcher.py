import re
from typing import List

def match(url: str, passUrls: List[str]):
    for pattern in passUrls:
        if re.match(pattern, url):
            return True
    return False