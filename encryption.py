import sys
move = 3
encrypted_char =""
ref_id = input("Enter Reference ID (should be 12 characters, alphanumeric or special characters(@#_$): ")
if len(ref_id) != 12 or not all(c.isalnum() or c in "@#_$" for c in ref_id):
    print("Invalid Reference ID")
    sys.exit()
else:
    encrypted_char =''.join([chr((ord(char) + move) % 127) if char.isalnum() or char in "@#_$" else char for char in ref_id])
    print("Reference ID encrypted:",encrypted_char)


choice = input("Do you want to decrypt it?(y/n): ").strip().lower()
print(move)
if choice == "y":
    decrypted_char =''.join([chr((ord(char) - move) % 127) if char.isalnum() or char in "@#_$" else char for char in encrypted_char])
    print("Reference ID decrypted:",decrypted_char)
else:
    print("Encryption Done")