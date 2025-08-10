# Step 1: Create an empty list called my_list
my_list = []
print("Step 1 - Created empty list:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("-" * 40)

# Step 2: Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2 - Appended elements 10, 20, 30, 40:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("-" * 40)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("Step 3 - Inserted 15 at index 1 (second position):")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: Index 1 is the second position (0-based indexing)")
print("-" * 40)

# Step 4: Extend my_list with another list [50, 60, 70]
extension_list = [50, 60, 70]
my_list.extend(extension_list)
print("Step 4 - Extended my_list with [50, 60, 70]:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: extend() adds each element individually, unlike append() which would add the entire list as one element")
print("-" * 40)

# Step 5: Remove the last element from my_list
removed_element = my_list.pop()
print("Step 5 - Removed the last element from my_list:")
print(f"Removed element: {removed_element}")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: pop() removes and returns the last element")
print("-" * 40)

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Step 7 - Found the index of value 30:")
print(f"Value 30 is at index: {index_of_30}")
print(f"my_list[{index_of_30}] = {my_list[index_of_30]}")
print(f"Final my_list = {my_list}")
print(f"Final length: {len(my_list)}")
print("-" * 40)
print("✅ All operations completed successfully!")