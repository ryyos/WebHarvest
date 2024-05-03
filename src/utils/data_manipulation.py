from typing import List, Dict

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


def search_key_v2(data: Dict[str, any], key: str, required_key: str = None) -> any:
    if key in data:
        if isinstance(data[key], dict):
            if required_key is None:
                return data[key]
            elif required_key in data[key]:
                return data[key][required_key]
        else:
            return None

    for k, v in data.items():
        if isinstance(v, dict):
            result = search_key_v2(v, key, required_key)
            if result is not None:
                return result
    return None

def search_key(data: Dict[str, any], key: str) -> any:
    if not isinstance(data, dict):
        return None
    if key in data:
        return data[key]
    for value in data.values():
        if isinstance(value, dict):
            result = search_key(value, key)
            if result is not None:
                return result

    return None
