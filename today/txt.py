from pathlib import Path
import re
from datetime import date

today = date.today()
# d1 = today.strftime("-%m-%d")
d1 = '-05-18'

working_dir = Path()
contents = []
for path in working_dir.glob("../*.txt"):
    with open(path.absolute(), encoding="utf-8") as f:
        content = f.read()
        rex = r"(.*?)\n.*?\d{4}" + r'{}'.format(d1)+ r"(.+)((?:\n.+)+)\d{4}-\d{2}-\d{2}"
        print(rex)
        all= re.findall(rex, content)
        for i in all:
            print(i)
    print(path.absolute())


# str="Test String which should \n end here \n Test  here String which should end here"

# print(re.findall(r'String which\b\n{0,}\b.*?here?', str))