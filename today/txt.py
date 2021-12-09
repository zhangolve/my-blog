from pathlib import Path
import re
from datetime import date

today = date.today()
d1 = today.strftime("-%m-%d")


working_dir = Path()
contents = []
for path in working_dir.glob("../*.txt"):
    with open(path.absolute(), encoding="utf-8") as f:
        content = f.read()
        my_regex = r"\d{4}-05-18"  + r"(.+)((?:\n.+)+)(\d{4}-\d{2}-\d{2})"
        m= re.findall(my_regex, content)
        print(m)
    print(path.absolute())


TEXTO = "Vaeeer"
subject = r"Var\boundary"

if re.search(rf"\b(?=\w){TEXTO}\\boundary(?!\w)", subject, re.IGNORECASE):
    print("match")

# print(re.search(rf"\b(?=\w){TEXTO}\\boundary(?!\w)", subject), re.IGNORECASE)