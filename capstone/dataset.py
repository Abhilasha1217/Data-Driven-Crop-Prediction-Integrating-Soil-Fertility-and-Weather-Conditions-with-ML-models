import pandas as pd
import random

states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
    "Uttar Pradesh","Uttarakhand","West Bengal"
]

crops = ["Rice","Wheat","Maize","Cotton","Sugarcane"]

data = []

for _ in range(2000):
    state = random.choice(states)

    if state in ["Kerala","Assam","West Bengal"]:
        temp = random.uniform(25, 35)
        rainfall = random.uniform(200, 350)
        crop = "Rice"

    elif state in ["Punjab","Haryana","Uttar Pradesh"]:
        temp = random.uniform(15, 30)
        rainfall = random.uniform(50, 150)
        crop = "Wheat"

    elif state in ["Maharashtra","Gujarat"]:
        temp = random.uniform(25, 38)
        rainfall = random.uniform(30, 120)
        crop = "Cotton"

    elif state in ["Karnataka","Tamil Nadu","Telangana"]:
        temp = random.uniform(25, 35)
        rainfall = random.uniform(50, 200)
        crop = "Maize"

    else:
        temp = random.uniform(20, 35)
        rainfall = random.uniform(50, 250)
        crop = random.choice(crops)

    N = random.randint(20, 120)
    P = random.randint(10, 100)
    K = random.randint(10, 150)
    ph = round(random.uniform(5.5, 8.5), 2)

    yield_val = round((temp * 0.1 + rainfall * 0.03 + N * 0.02), 2)

    data.append([state, N, P, K, temp, rainfall, ph, crop, yield_val])

df = pd.DataFrame(data, columns=[
    "State","N","P","K","temperature","rainfall","ph","Crop","Yield"
])

df.to_csv("final_dataset.csv", index=False)

print("Dataset created successfully!")