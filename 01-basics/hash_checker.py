import hashlib
Message = "ThalesSecurity2026"
message_bytes = message.encode('utf-8')
sha256_hash = hashlib.sha256(message_bytes).hexdigest()
print("original text:", message)
print("SHA=256 Hash :", sha256_hash

      modified_message = "ThalesSecurity2027"
modified_hash = hashlib.sha256(modified_message.encode('utf-8')).hexdigest()

print ("\nModified text:", modified_message)
print("New SHA-256 :", modified_hash)
