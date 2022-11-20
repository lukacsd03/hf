import re

with open("hazi.txt",'r') as novella, open("ki.txt",'w') as f:
    for x in novella:
        if (x.strip()):
            x: re.sub('r+','', x)
            x = x.replace('a',"")
            x = x.replace('á',"")
            x = x.replace('i',"")
            x = x.replace('í',"")
            x = x.replace('e',"")
            x = x.replace('é',"")
            x = x.replace('o',"")
            x = x.replace('ó',"")
            x = x.replace('ö',"")
            x = x.replace('ő',"")
            x = x.replace('u',"")
            x = x.replace('ú',"")
            x = x.replace('ü',"")
            x = x.replace('ű',"")
            x = x.replace('.',"")
            x = x.replace('?',"")
            x = x.replace('!',"")
            x = x.replace(',',"")
            x = x.replace('"',"")

            f.write(x)
