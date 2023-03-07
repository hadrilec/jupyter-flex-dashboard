
This repo contains a toy example on how to create a jupyter flex notebook from python.
After compilation, an html flex dashboard report is created.



``` python
# download librairies
pip install -r requirements.txt

# make flex notebook
python make_flex_notebook.py

# make flex dashboard html report
jupyter nbconvert --to flex REPORT_SUMMARY.ipynb --execute
```


![](screenshot.PNG)
