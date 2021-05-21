import numpy as np
import pandas as pd

df = pd.read_csv("Personalised/506521_leak.csv", delimiter=',', header= None, names=["time", "nonce", "key"])

df.head()

df["time"][1]
df["nonce"][1]
df["key"][1]

for i in range 1:
    bitLength = df["nonce"][i]
    bitLength.bit_length()
    print(bitLength)