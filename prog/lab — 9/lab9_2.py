def calculate_waiting_time(service_times):
    waiting_times = []
    total_time = 0
    
    for time in service_times:
        waiting_times.append(total_time)
        total_time += time
        
    return waiting_times

n = int(input("Введите количество покупателей: "))
service_times = []

for i in range(n):
    t = int(input(f"Введите время обслуживания покупателя {i + 1}: "))
    service_times.append(t)

waiting_times = calculate_waiting_time(service_times)
print(f"Время пребывания каждого покупателя в очереди: {waiting_times}")
