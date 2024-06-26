import hashlib
import json

def stringify(data):
    return json.dumps(data)
def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_data=sorted(map(lambda data: json.dumps(data), args))
    #print(f'args:{stringified_data}')
    joined_data=''.join(stringified_data)
    #print(f'joined_data:{joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    print(f"crypto_hash(1,2,[3]): {crypto_hash(2,1,[3])}")

