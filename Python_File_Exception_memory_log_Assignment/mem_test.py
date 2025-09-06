from memory_profiler import profile

# Use the @profile decorator to monitor memory usage
@profile
def create_large_list():
    # Create a large list
    my_list = [i for i in range(100000)]
    print("List created with 100,000 elements")
    return my_list

if __name__ == "__main__":
    my_list = create_large_list()
