import time

def cubic_algorithm(n):
    """Example cubic algorithm: triple nested loop"""
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1 
    return count

# Values of n to test
n_values = [100, 200, 400, 800]

print(f"{'n':<6}{'Experimental Time (s)':<25}{'n^3':<15}{'T(n)/n^3':<15}")
for n in n_values:
    start_time = time.time()
    cubic_algorithm(n)
    end_time = time.time()

    experimental_time = end_time - start_time
    theoretical_n3 = n ** 3   
    normalized_time = experimental_time / theoretical_n3

    print(f"{n:<6}{experimental_time:<25.5f}{theoretical_n3:<15}{normalized_time:<15.2e}")
