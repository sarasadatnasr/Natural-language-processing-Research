from __future__ import unicode_literals
import json
from negar.virastar import PersianEditor
from hazm import *


with open('formal.txt','r',encoding='utf-8-sig') as txt_file:
    with open("text.json",'w',encoding="utf-8-sig") as file:
      for x in txt_file:    
        if '*' in x:
          dictionary={'challenge ': x}
          json.dump(dictionary, file, indent = 1, sort_keys = False,ensure_ascii=False)
          file.write('\n')
        elif '*' not in x:  
          orginal = x
          normal = str(PersianEditor(x))
          tokens = word_tokenize(normal)
          dictionary = {
            "orginal": orginal ,
            "normal": normal,
            "tokens": tokens,}
          json.dump(dictionary, file, indent = 2, sort_keys = False,ensure_ascii=False)
          file.write('\n')
          
