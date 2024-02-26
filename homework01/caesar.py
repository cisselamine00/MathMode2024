import typing as tp
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
            shifted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') - shift) % 26
            shifted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
def caesar_breaker(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker("python", d)
    0
    >>> caesar_breaker("sbwkrq", d)
    3
    """
    best_shift = 0
    max_matches = 0
    for shift in range(26):
        matches = 0
        decrypted = decrypt_caesar(ciphertext, shift)
        for word in decrypted.split():
            if word.lower() in dictionary:
                matches += 1
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
    return best_shift
