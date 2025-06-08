n = int(input("Enter the value >>> "))

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(f"{hours}h : {minutes}m : {seconds}s")