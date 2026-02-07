import sys
import pandas as pd

print('arguemtns: ', sys.argv )

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

month = int(sys.argv[1])
df["month"] = month
print(df.head()) 

df.to_parquet(f"output_{month}parquet.parquet")

 
print(f'hello world, month = {month}')