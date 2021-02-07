import csv
import math
import numpy as np
import pandas as pd
from IPython.display import display, HTML 
from os import path
from collections import Counter
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as mplot 
import plotly.express as px 

df = pd.read_csv("C:\\Users\\clwir\\Web-Development\\dynamic-goals\\TimeInNew.csv")

time_new = []
new_do_not_proceed = []
dn = "date in Do not Proceed"
n = "date in New"
nr = "date in Not Reviewed"
x = "date in Calibrating"
y = "date in Considered by Recruiter"
z = "date in Hiring Manager Candidate First Review"

def time_from_new():
    days1 = n-x
    for x in "Calibrating":
        if x <= y or x <= z or x <= dn:
            time_new.append(days1)

if x in "Calibrating" == True:
    time_from_new()
elif x in "Calibrating" == False:
    days2 = dn-n
    new_do_not_proceed.append(days2)
else:
    days3 = nr-n
    new_do_not_proceed.append(days3)
    
time_new.extend(new_do_not_proceed)

print(time_new)