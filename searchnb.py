#Search string
search_string = "conda env"

#Search current directory
directory ='.'

import os  
import os.path
from IPython.core.display import display, HTML

search_string = search_string.lower()
links=[]

files = os.listdir(directory)
files.sort()
for fn in files:
    if 'ipynb' in fn:
        filename = f"{directory}/{fn}"
        if os.path.isfile(filename):
            found = False
            with open(filename,'r') as fp:
                for line in fp:
                    line = line.lower()
                    if search_string in line:
                        links.append("<a href="+fn+" target=\"_blank\" >"+fn+"</a></br>")
                        break
if links:
    print(' '.join(links))
else:
    print('string ('+search_string+') not found.')
            