import surprise
surprise.__version__


import numpy
print(numpy.__version__)

import numpy as np
import pandas as pd
import streamlit as st
print(np.__version__)
print(pd.__version__)
print()

import sys
print(sys.executable)


import sys
print("Running Python from:", sys.executable)

from tmdbv3api import Movie, TMDb



import pickle

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

print(type(movies))
print(type(cosine_sim))
