import math

def calculate_arc_length(radius, angle):
    return 2 * math.pi * radius * (angle / 360)

R1, R2, R3 = 5, 10, 7  
alpha, beta, gamma = 90, 180, 45  

# Вычисляем длины дуг
L1 = calculate_arc_length(R1, alpha)
L2 = calculate_arc_length(R2, beta)
L3 = calculate_arc_length(R3, gamma)

# Выводим результаты
print(f"Длина дуги первого сектора (R1={R1}, α={alpha}°): {L1:.2f}")
print(f"Длина дуги второго сектора (R2={R2}, β={beta}°): {L2:.2f}")
print(f"Длина дуги третьего сектора (R3={R3}, γ={gamma}°): {L3:.2f}")