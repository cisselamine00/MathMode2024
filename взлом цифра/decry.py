def calculate_letter_frequencies(text):
    frequencies = {}
    total_letters = 0

    for char in text:
        if char.isalpha():  # Vérifier si le caractère est une lettre
            char = char.lower()  # Convertir en minuscule
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
            total_letters += 1

    # Convertir les comptages en fréquences
    for char, count in frequencies.items():
        frequencies[char] = count / total_letters

    return frequencies

# Lire le texte chiffré depuis le fichier
with open('cipher.txt', 'r') as file:
    cipher_text = file.read()

# Calculer les fréquences des lettres dans le texte chiffré
letter_frequencies = calculate_letter_frequencies(cipher_text)

# Afficher les fréquences des lettres
print("Fréquences des lettres dans le texte chiffré :")
for char, freq in sorted(letter_frequencies.items()):
    print(char, ':', freq)
