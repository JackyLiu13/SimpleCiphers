def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Preserve case
            is_upper = char.isupper()
            # Convert to lowercase for easier manipulation
            char = char.lower()
            # Apply shift
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # Convert back to original case
            if is_upper:
                shifted = shifted.upper()
            encrypted_text += shifted
        else:
            # Leave non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

# Example usage:
plain_text = "Hello, World!"
shift_amount = 3
encrypted_text = caesar_cipher(plain_text, shift_amount)
print("Encrypted text:", encrypted_text)

# Decryption:
decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print("Decrypted text:", decrypted_text)
