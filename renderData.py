import pandas as pd
import numpy as np
ab = pd.read_csv("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Βάσεις Δεδομένων/GitWithMyLove/data/AB.csv")
#lengths = [len(x) for x in len(set(ab["category"]))]
print(ab['category'][0],ab['name'][0] )