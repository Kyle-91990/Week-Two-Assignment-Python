def modify_list():
    # Step 1: Create an empty list
    my_list = []

    # Step 2: Append elements 10, 20, 30, 40
    my_list.append(10)  # Adds 10 to the end of the list
    my_list.append(20)  # Adds 20 to the end of the list
    my_list.append(30)  # Adds 30 to the end of the list
    my_list.append(40)  # Adds 40 to the end of the list

    # Step 3: Insert 15 at the second position (index 1)
    my_list.insert(1, 15)  # Inserts 15 at index 1

    # Step 4: Extend my_list with another list [50, 60, 70]
    my_list.extend([50, 60, 70])  # Adds 50, 60, and 70 to the end of the list

    # Step 5: Remove the last element
    my_list.pop()  # Removes the last element (70) from the list

    # Step 6: Sort my_list
    my_list.sort()

    # Step 7: Find the index of 30
    index_30 = my_list.index(30)  # Finds the index of the value 30

    # Print the index of 30
    print(f"Index of 30: {index_30}")  # Index of 30: 3

    # Print the final list and index of 30
    print(f"My list: {my_list}")  # My list: [10, 15, 20, 30, 40, 50, 60]
    print(f"Index of 30: {index_30}")  # Index of 30: 3

if __name__ == "__main__":
    modify_list()