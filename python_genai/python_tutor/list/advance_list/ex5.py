sports = ["Soccer", "Basketball", "Baseball", "Tennis", "Cricket"]
print("Original list:", sports)
sports[1:1] = ["Volleyball", "Rugby", "Badminton"]  # Inserts new sports at index 1
print("Updated list:", sports)
print("Length of updated list:", len(sports))