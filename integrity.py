import hashlib

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def verify_integrity(original_data, hashed_data):
    calculated_hash = calculate_hash(original_data)
    if calculated_hash == hashed_data:
        return True
    else:
        return False

# Original data
data = input("Enter your plain text: ")

# Calculate the hash of the original data
hash_value = calculate_hash(data)

# Tamper with the data (simulate data modification)
tampered_data = data + " - Tampered!"

# Verify the integrity of the tampered data
is_integrity_verified = verify_integrity(tampered_data, hash_value)

print("Original Data:", data)
print("Hash Value:", hash_value)
print("Tampered Data:", tampered_data)
print("Integrity Verified:", is_integrity_verified)