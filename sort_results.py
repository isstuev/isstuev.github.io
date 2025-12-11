def sort_results():
    # Read the results
    with open('url_test_results.txt', 'r') as f:
        results = [line.strip() for line in f.readlines()]
    
    # Sort results by status
    success_results = []
    error_results = []
    too_long_results = []
    
    for result in results:
        if ' | success' in result:
            success_results.append(result)
        elif ' | error' in result:
            error_results.append(result)
        elif ' | too long' in result:
            too_long_results.append(result)
    
    # Write sorted results to a new file
    with open('sorted_results.txt', 'w') as f:
        # Write success results
        f.write("=== SUCCESS RESULTS ===\n")
        f.write(f"Total: {len(success_results)}\n\n")
        for result in success_results:
            f.write(f"{result}\n")
        
        # Write error results
        f.write("\n=== ERROR RESULTS ===\n")
        f.write(f"Total: {len(error_results)}\n\n")
        for result in error_results:
            f.write(f"{result}\n")
        
        # Write too long results
        f.write("\n=== TOO LONG RESULTS ===\n")
        f.write(f"Total: {len(too_long_results)}\n\n")
        for result in too_long_results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    sort_results() 