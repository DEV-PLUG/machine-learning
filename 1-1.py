import matplotlib.pyplot as plt
import numpy as nm
import pandas as pd
import sklearn.linear_model

oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")

