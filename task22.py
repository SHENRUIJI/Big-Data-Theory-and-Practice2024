from multiprocessing import Pool
import time
from tqdm import tqdm

def calculate(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num = num // i
        else:
            i += 1
    if num > 1:
        factors.append(num)
    return len(factors)  

def main():
    with open('data2.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    start_time = time.time()  


    results = []
    with Pool(2) as pool:
        # 使用tqdm
        for result in tqdm(pool.imap(calculate, numbers), total=len(numbers), desc="Processing numbers"):
            results.append(result)

    end_time = time.time() 
    tt_time = end_time - start_time  

    print(f"Total number of factors: {sum(results)}")
    print(f"Total execution time: {tt_time:.2f} seconds")

if __name__ == '__main__':
    main()
