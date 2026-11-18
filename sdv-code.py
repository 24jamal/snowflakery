import pandas as pd

data = pd.DataFrame({
    "age": [22, 25, 30, 35, 40, 45, 50, 28, 32, 38],
    "salary": [20000, 25000, 35000, 45000, 50000,
               60000, 75000, 30000, 40000, 48000],
    "city": [
        "Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai",
        "Delhi", "Chennai", "Mumbai", "Delhi", "Chennai"
    ],
    "is_customer": [
        True, True, False, True, False,
        True, True, False, True, False
    ]
})

print(data)
print("-----------------------------------------")
