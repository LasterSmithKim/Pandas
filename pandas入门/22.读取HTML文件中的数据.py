import numpy as np
import pandas as pd
import urllib.request
import ssl

req = urllib.request.Request('https://en.wikipedia.org/wiki/Udacity')
context = ssl._create_unverified_context()
response = urllib.request.urlopen(req,context=context)
df = pd.read_html(response)
print(df[1])