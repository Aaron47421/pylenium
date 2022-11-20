# pylenium
an open-source module designed to help improve workflow for selenium users. 

DOCUMENTATION.

1. ```git clone git@github.com:Aaron47421/pylenium.git``` to clone the repo.
2. run requirements.bat or `pip install -r requirements.txt`
3. run the install.py and this will auto install it to your python Lib directory.

that's it.

here's an example.
```
from pylenium.chrome import newbrowser

driver = newbrowser(headless=False, detached=True)
driver.get("https://google.com")
```
