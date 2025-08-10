# PLPPythonAssignmentWeek2
PLP Python Module Assignment Week 2
Description:
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.


# Step 1: Create an empty list called my_list
my_list = []
print("Step 1 - Created empty list:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("-" * 40)
Step 1 - Created empty list:
my_list = []
Length: 0
----------------------------------------
# Step 2: Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2 - Appended elements 10, 20, 30, 40:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("-" * 40)
Step 2 - Appended elements 10, 20, 30, 40:
my_list = [10, 20, 30, 40]
Length: 4
----------------------------------------
# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("Step 3 - Inserted 15 at index 1 (second position):")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: Index 1 is the second position (0-based indexing)")
print("-" * 40)
Step 3 - Inserted 15 at index 1 (second position):
my_list = [10, 15, 20, 30, 40]
Length: 5
Note: Index 1 is the second position (0-based indexing)
----------------------------------------
# Step 4: Extend my_list with another list [50, 60, 70]
extension_list = [50, 60, 70]
my_list.extend(extension_list)
print("Step 4 - Extended my_list with [50, 60, 70]:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: extend() adds each element individually, unlike append() which would add the entire list as one element")
print("-" * 40)
Step 4 - Extended my_list with [50, 60, 70]:
my_list = [10, 15, 20, 30, 40, 50, 60, 70]
Length: 8
Note: extend() adds each element individually, unlike append() which would add the entire list as one element
----------------------------------------
# Step 5: Remove the last element from my_list
removed_element = my_list.pop()
print("Step 5 - Removed the last element from my_list:")
print(f"Removed element: {removed_element}")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: pop() removes and returns the last element")
print("-" * 40)
Step 5 - Removed the last element from my_list:
Removed element: 70
my_list = [10, 15, 20, 30, 40, 50, 60]
Length: 7
Note: pop() removes and returns the last element
----------------------------------------
# Step 6: Sort my_list in ascending order
print("Before sorting:")
print(f"my_list = {my_list}")
my_list.sort()
print("\nStep 6 - Sorted my_list in ascending order:")
print(f"my_list = {my_list}")
print(f"Length: {len(my_list)}")
print("Note: sort() modifies the list in-place")
print("-" * 40)
Before sorting:
my_list = [10, 15, 20, 30, 40, 50, 60]

Step 6 - Sorted my_list in ascending order:
my_list = [10, 15, 20, 30, 40, 50, 60]
Length: 7
Note: sort() modifies the list in-place
----------------------------------------
# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Step 7 - Found the index of value 30:")
print(f"Value 30 is at index: {index_of_30}")
print(f"my_list[{index_of_30}] = {my_list[index_of_30]}")
print(f"Final my_list = {my_list}")
print(f"Final length: {len(my_list)}")
print("-" * 40)
print("✅ All operations completed successfully!")
Step 7 - Found the index of value 30:
Value 30 is at index: 3
my_list[3] = 30
Final my_list = [10, 15, 20, 30, 40, 50, 60]
Final length: 7
----------------------------------------
✅ All operations completed successfully!
# Summary of all operations performed
print("=" * 50)
print("📋 SUMMARY OF LIST OPERATIONS")
print("=" * 50)
print("1. ✅ Created empty list: []")
print("2. ✅ Appended 10, 20, 30, 40: [10, 20, 30, 40]")
print("3. ✅ Inserted 15 at index 1: [10, 15, 20, 30, 40]")
print("4. ✅ Extended with [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]")
print("5. ✅ Removed last element (70): [10, 15, 20, 30, 40, 50, 60]")
print("6. ✅ Sorted in ascending order: [10, 15, 20, 30, 40, 50, 60]")
print("7. ✅ Found index of 30: index 3")
print("=" * 50)
print(f"🎯 FINAL RESULT: my_list = {my_list}")
print(f"📊 Total elements: {len(my_list)}")
print("=" * 50)
==================================================
📋 SUMMARY OF LIST OPERATIONS
==================================================
1. ✅ Created empty list: []
2. ✅ Appended 10, 20, 30, 40: [10, 20, 30, 40]
3. ✅ Inserted 15 at index 1: [10, 15, 20, 30, 40]
4. ✅ Extended with [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]
5. ✅ Removed last element (70): [10, 15, 20, 30, 40, 50, 60]
6. ✅ Sorted in ascending order: [10, 15, 20, 30, 40, 50, 60]
7. ✅ Found index of 30: index 3
==================================================
🎯 FINAL RESULT: my_list = [10, 15, 20, 30, 40, 50, 60]
📊 Total elements: 7
==================================================
[SUCCESS] Execution Complete
Task Completion Summary: Successfully completed all list operations as requested. Created a comprehensive Python script demonstrating each list operation step by step with clear explanations and output showing the state of the list after each operation.

Approaches Used:

Python list methods: append(), insert(), extend(), pop(), sort(), index()
Step-by-step execution with detailed output
Clear documentation and explanations for each operation
Challenges Overcome: No significant challenges encountered

