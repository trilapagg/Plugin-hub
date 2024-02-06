import hashlib
import os

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def hash_jar_files_in_directory(directory_path, output_file):
    with open(output_file, "w") as hashes_file:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".jar"):
                    file_path = os.path.join(root, file)
                    sha256_hash = calculate_sha256(file_path)
                    hashes_file.write(f"{file}:{sha256_hash}\n")
                    print(f"Processed {file}")

# Replace 'trilapagg' with the actual path to your directory
directory_path = 'trilapagg'
# Output file
output_file = 'hashes.txt'

hash_jar_files_in_directory(directory_path, output_file)
print(f"Hashes have been written to {output_file}")
