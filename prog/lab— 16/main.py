import math

def calculate_arc_lengths(R1, R2, R3, alpha, beta, gamma):
    L1 = 2 * math.pi * R1 * (alpha / 360)
    L2 = 2 * math.pi * R2 * (beta / 360)
    L3 = 2 * math.pi * R3 * (gamma / 360)
    return (L1, L2, L3)

R1, R2, R3 = 2, 3, 1
alpha, beta, gamma = 180, 90, 360
lengths = calculate_arc_lengths(R1, R2, R3, alpha, beta, gamma)

print(f"Длины дуг: L1={lengths[0]:.2f}, L2={lengths[1]:.2f}, L3={lengths[2]:.2f}")