
from typing import List

def split_list(datas: List[any], length_each: int):
    results: List[any] = []
    for i in range(0, len(datas), length_each):
        results.append(datas[i:i+length_each])
    return results

def to_float(text: str) -> float | str:
    try:
        return float(text)
    except Exception:
        return text
    

def to_int(text: str) -> float | str:
    try:
        return int(text)
    except Exception:
        return text
    
def val(text: any) -> any:
    if text: return text
    else: return None

def vlist_dict(data_list, key):
    seen = set()
    result = []
    for d in data_list:
        if d[key] not in seen:
            seen.add(d[key])
            result.append(d)
    return result