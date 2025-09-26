import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')



def cubic_algorithm(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count

n_values = [100, 200, 400, 800]
experimental_time = []

for n in n_values:
    start = time.time()
    cubic_algorithm(n)
    end = time.time()
    experimental_time.append(end - start)

theoretical_time = [n**3 for n in n_values]
normalized_time = [experimental_time[i]/theoretical_time[i] for i in range(len(n_values))]

# Experimental vs n
plt.figure(figsize=(8,5))
plt.plot(n_values, experimental_time, 'o-', label='Experimental Time')
plt.plot(n_values, theoretical_time, 's--', label='Theoretical n^3 (scaled)')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Experimental vs Theoretical Time')
plt.legend()
plt.grid(True)
plt.show()

# Normalized time vs n
plt.figure(figsize=(8,5))
plt.plot(n_values, normalized_time, 'o-', color='green')
plt.xlabel('n')
plt.ylabel('Normalized Time T(n)/n^3')
plt.title('Normalized Time vs n')
plt.grid(True)
plt.show()
