# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
transactions_joined_prepared = dataiku.Dataset("transactions_joined_prepared")
df = transactions_joined_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_new = df.drop('authorized_flag', axis=1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_new.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
fkdls = dataiku.Dataset("fkdls")
fkdls.write_with_schema(df_new)