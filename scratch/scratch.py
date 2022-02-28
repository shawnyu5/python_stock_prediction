import pandas as pd
import numpy as np

docs = {"computer": {"1": 1, "3": 5, "8": 2}, "politics": {"0": 2, "1": 2, "3": 1}}
# Creates a dataframe with keys as index and values as cell values.
df = pd.DataFrame(docs)

# Create a new set of index from min and max of the dictionary keys.
new_index = np.arange(int(df.index.min()), int(df.index.max())).astype(str)

# Add the new index to the existing index and fill the nan values with 0, take a transpose of dataframe.
new_df = df.reindex(new_index).fillna(0).T.astype(int)

print(f" new_df: {str(new_df)}")  # __AUTO_GENERATED_PRINT_VAR__
