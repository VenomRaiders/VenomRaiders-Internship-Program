def main(test_cases):
    results = []

    def get_sum(test_cases):        
        if test_cases != 0:
            X = int(input())  # Number of integers in the test case
            ss_integers = list(map(int, input().split()))[0:X] # List of spaced-separated integers
            # Calculate the sum of squares of positive integers (excluding negatives)
            total_sum = sum(
                map(lambda x:x ** 2, filter(lambda x:x > 0, ss_integers))
            )
            results.append(total_sum)
            return get_sum(test_cases - 1)
        return

    get_sum(test_cases)
    
    return results

if __name__ == "__main__":
    N = int(input())  # Number of test cases
    output = main(N)
    print(*output, sep = "\n")


