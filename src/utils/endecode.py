import hashlib

class Endecode:

    @staticmethod    
    def md5_hash(text: str):
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()