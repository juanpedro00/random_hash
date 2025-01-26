import hashlib
import random
import string

def generate_random_string(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_hash():
    for _ in range(1000):
        random_string = generate_random_string()
        hash_value = hashlib.sha256(random_string.encode()).hexdigest()
        if hash_value.startswith("00"):
            print(f"Found hash: {hash_value}")
            return True
    print("No valid hash found after 1000 attempts.")
    return False

if __name__ == "__main__":
    exit(0 if find_hash() else 1)
