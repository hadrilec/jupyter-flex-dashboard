
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:01:47 2022

@author: hleclerc
"""

import nbformat as nbf

nb = nbf.v4.new_notebook()

params = """\
flex_title = "SUMMARY"
"""

nb['cells'] += [nbf.v4.new_code_cell(params)]
nb['cells'][0]['metadata'] = {"tags": ["parameters"]}

#
# Sidebar
#

text = """\
# Sidebar
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["sidebar"]}

text = """\
###  
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

code = """\
from IPython.display import SVG, display

import os
folder = './'
os.chdir(folder)

"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["source"]}

text = """\
[![](pict.png)](https://www.wikipedia.org/)

"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}

text = """\
Ratio = $\sum{A_{i,t}}{i}$
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}


#
# First Page
#

text = """\
# Page 1
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

text = """\
## Col1
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

text = """\
### Simple scatter
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

code = """\
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig1 = px.pie(df, values='pop', names='country', title='Population of European continent')

"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["source"]}

code = """\
fig1.show()
"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}

code = """\
import plotly.graph_objects as go
fig2 = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)

"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["source"]}


text = """\
## Col2
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

text = """\
### Simple scatter2
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

code = """\

"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["source"]}

code = """\
fig2.show()
"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}

#
# Second page
#

text = """\
# page 2
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

text = """\
## Col1
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["tabs"]}

code = """\

"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["source"]}


text = """\
### tab 1
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]


code = """\
fig2.show()
"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}

text = """\
### tab2
"""
nb['cells'] += [nbf.v4.new_markdown_cell(text)]

code = """\
fig1.show()
"""
nb['cells'] += [nbf.v4.new_code_cell(code)]
nb['cells'][len(nb['cells'])-1]['metadata'] = {"tags": ["body"]}

import os
folder = './'
os.chdir(folder)

fname = 'REPORT_SUMMARY.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)



