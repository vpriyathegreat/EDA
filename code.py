import streamlit as st

import numpy as np
import pandas as pd



from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

st.write('Hello world!')
import pandas as pd

# Specify the public URL of the CSV file
csv_url = "https://drive.google.com/file/d/1N_zdNog3SUy1JKTvO1RybBbSrTyuFttj/view?usp=sharing"

# Read the CSV file from the URL
ds = pd.read_csv(csv_url, quoting=3, on_bad_lines='skip')
