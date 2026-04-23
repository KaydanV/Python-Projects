# Set Operations on Names
# Reads two files, each containing a list of names (one per line)
# Performs union, intersection, and difference operations

def read_names_from_file(filename):
    """Read names from a text file and return a set of names."""
    try:
        with open(filename, 'r') as file:
            # Strip whitespace and convert to a set (removes duplicates)
            names = {line.strip() for line in file if line.strip()}
        return names
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return set()

def main():
    # Input file names
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    # Read names into sets
    set1 = read_names_from_file(file1)
    set2 = read_names_from_file(file2)

    # Display the sets
    print("\nSet 1:", set1)
    print("Set 2:", set2)

    # Perform set operations
    union_set = set1 | set2
    intersection_set = set1 & set2
    difference_set = set1 - set2

    # Display results
    print("\n--- Set Operations ---")
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference (Set1 - Set2):", difference_set)

if __name__ == "__main__":
    main()
