n = int(input())
positive = []
negative = []

for i in range(n):
    current_number = int(input())
    if current_number < 0:
        negative.append(current_number)
    else:
        positive.append(current_number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")