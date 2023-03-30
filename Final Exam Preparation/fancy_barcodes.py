import re
pattern = r"@#+[A-Z][A-Za-z\d]{4,}[A-Z]@#+"

n = int(input())

for _ in range(n):
    barcode = input()

    matches = re.findall(pattern, barcode)
    if matches:
        product_group = ""
        is_digit = re.findall(r"\d", barcode)
        if is_digit:
            for match in is_digit:
                product_group += match
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")