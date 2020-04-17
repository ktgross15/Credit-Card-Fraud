# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
unseen_scored = dataiku.Dataset("unseen_scored")
df = unseen_scored.get_dataframe()

df['new'] = 'new stuff yay'

# Write recipe outputs
unseen_python = dataiku.Dataset("unseen_python")
unseen_python.write_with_schema(unseen_python_df)
