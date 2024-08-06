import random

# Simulating input for 100 random test cases
test_cases = 100
test_input = [
    f"{X}\n{' '.join(str(random.randint(-100, 100)) for _ in range(X))}"
    for X in [random.randint(1, 100) for _ in range(test_cases)]
]

def main(test_cases):
    results = []
    for i in range(len(test_input)):     
        X = int(test_input[i].split("\n")[0])  # Number of integers in the test case
        ss_integers = list(map(int, test_input[i].split("\n")[-1].split()))[0:X] # List of spaced-separated integers
        # Calculate the sum of squares of positive integers (excluding negatives)
        total_sum = sum(
            map(lambda x:x ** 2, filter(lambda x:x > 0, ss_integers))
        )
        results.append(total_sum)

    return results

if __name__ == "__main__":
    N = 100  # Number of test cases
    output = main(N)
    print(*output, sep = "\n")






