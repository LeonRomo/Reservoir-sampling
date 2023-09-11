import random

def reservoir_sampling(stream, M):
    """
    stream: iterator (or list) for data stream.
    M: size of the reservoir (desired sample size).
    """
    # Step 1: Initialize the reservoir with the first M elements
    reservoir = [next(stream) for _ in range(M)]
    
    # Step 2: Process the rest of the elements
    for n, element in enumerate(stream, start=M+1):
        # Select a random integer between 0 and n (both inclusive)
        j = random.randint(0, n)
        # If the random integer is less than M, replace the j-th element in reservoir
        if j < M:
            reservoir[j] = element
            
    return reservoir

# Sample usage
stream_data = iter(range(1000))  # This simulates a stream of data from 0 to 999
sample_size = 10
sample = reservoir_sampling(stream_data, sample_size)
print(sample)
