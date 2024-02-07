import hashlib
import os
import json

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def generate_jar_file_info(directory_path):
    jar_files_info = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".jar"):
                file_path = os.path.join(root, file)
                file_info = {
                    "internalName": file.replace('.jar', ''),
                    "hash": calculate_sha256(file_path),
                    "size": os.path.getsize(file_path),
                    "plugins": [f"com.{file.replace('.jar', '')}.{file.capitalize().replace('.jar', 'Plugin')}"],
                    "displayName": "Tril" + file.replace('.jar', '').capitalize(),
                    "description": "",
                    "provider": "trilapagg"
                }
                jar_files_info.append(file_info)
    return jar_files_info

# Replace 'trilapagg' with the actual path to your directory
directory_path = 'trilapagg'

jar_files_info = generate_jar_file_info(directory_path)

# Convert the list to JSON format
json_output = json.dumps(jar_files_info, indent=2)

# Optionally, write to a file
output_file = 'plugins.json'
with open(output_file, 'w') as f:
    f.write(json_output)

print(f"JSON data has been written to {output_file}")
