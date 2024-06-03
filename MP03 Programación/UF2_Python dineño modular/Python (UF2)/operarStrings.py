def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

original = "Hola mundo"
reversed_str = reverse_string(original)
print("Original:", original)
print("Invertido:", reversed_str)
# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————
def sort_string(s):
    if len(s) <= 1:
        return s
    else:
        pivot = s[0]
        lesser = sort_string(''.join(c for c in s[1:] if c < pivot))
        greater = sort_string(''.join(c for c in s[1:] if c >= pivot))
        return lesser + pivot + greater

original = "computadora"
sorted_str = sort_string(original)
print("Original:", original)
print("Ordenado:", sorted_str)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————
def sort_vowels_consonants(s):
    vowels = ""
    consonants = ""
    for char in s:
        if char.lower() in "aeiou":
            vowels += char
        else:
            consonants += char
    return vowels + consonants

original = "python"
sorted_vc = sort_vowels_consonants(original)
print("Original:", original)
print("Ordenado:", sorted_vc)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————
def separate_vowels_consonants(s):
    if len(s) == 0:
        return "", ""
    else:
        vowels, consonants = separate_vowels_consonants(s[1:])
        if s[0].lower() in "aeiou":
            return s[0] + vowels, consonants
        else:
            return vowels, s[0] + consonants

# Ejemplo de uso:
original = "hello"
vowels, consonants = separate_vowels_consonants(original)
print("Original:", original)
print("Vocales:", vowels)
print("Consonantes:", consonants)