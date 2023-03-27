string = input().split("\\")

file_args = string[-1]
extensions = file_args.split(".")
new = extensions.pop()
print(new)
print(f"File name: {extensions[-2]}")
print(f"File extension: {extensions[-1]}")

