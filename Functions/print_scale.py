def print_scale(sine_value):
    """Функція для виведення шкали для синусоїдальних значень"""
    
    # Визначаємо кількість символів для виведення шкали
    scale_length = 10  # Довжина шкали
    scaled_value = int((sine_value + 1) * (scale_length // 2))  # Масштабуємо значення до довжини шкали

    # Створюємо шкалу
    scale = '|' * scaled_value + ' ' * (scale_length - scaled_value)
    
    # Виводимо шкалу
    print(f"Value: {sine_value:.4f} | {scale}")