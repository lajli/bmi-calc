# chmod_analyzer.py
# Автор: [Мурзабаева Л.Т.]
# Вариант 13

def octal_to_binary_triad(octal_digit):
    """Переводит восьмеричную цифру в двоичную триаду."""
    binary = bin(int(octal_digit))[2:].zfill(3)
    return binary

def binary_to_rwx(binary_triad):
    """Переводит двоичную триаду в строку rwx."""
    permissions = ""
    mapping = [('r', 2), ('w', 1), ('x', 0)]
    for char, bit in mapping:
        if binary_triad[bit] == '1':
            permissions += char
        else:
            permissions += '-'
    return permissions

def analyze_chmod():
    print("=== Анализатор прав доступа Unix ===")
    
    while True:
        octal_input = input("Введите трехзначное восьмеричное число (например, 750): ").strip()
        
        if len(octal_input) != 3 or not octal_input.isdigit():
            print("Ошибка: введите ровно три цифры.")
            continue
        
        if any(digit not in '01234567' for digit in octal_input):
            print("Ошибка: число должно быть восьмеричным (цифры 0-7).")
            continue
        
        print(f"\nАнализ прав доступа для {octal_input}:")
        
        binary_parts = []
        rwx_parts = []
        
        for digit in octal_input:
            binary = octal_to_binary_triad(digit)
            rwx = binary_to_rwx(binary)
            binary_parts.append(binary)
            rwx_parts.append(rwx)
        
        print(f"Двоичное представление: {' '.join(binary_parts)}")
        print(f"Формат rwx: {''.join(rwx_parts)}")
        
        break

if __name__ == "__main__":
    analyze_chmod()