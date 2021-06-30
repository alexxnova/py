import json
import pandas as pd
import os
from collections import Counter
import re

 
class ArticleJSON():
    
    def __init__(self, csvPath, jsonPath):
        self.csvPath = csvPath
        self.jsonPath = jsonPath
        self.listWords=[]
 
    def most_used_words(self,content, numTopWords):
        words=re.findall(r"[\w']+",content)
        articleWords=[word.lower() for word in words if len(word)>4]
        countWords=Counter(articleWords) 
        mostUsed=dict(countWords.most_common(numTopWords))
        return (mostUsed)
    
    def remove_character(self,content):
        listCharacter=[r"[" , r"\\xa0" ,  r"\\n", "]", r"'", r"\n", r"\xa0"]
        for ch in listCharacter:
            content=content.replace(ch,"")
        return content
 
    def format_data(self):
        numTopWords=3
        numParagraphs=3
        numContentCol=2

        csvData = pd.read_csv(self.csvPath)
        contentColName=list(csvData.columns)[numContentCol]

        for i in range(0,len(csvData.index)):
            self.listWords.append(self.most_used_words(csvData[contentColName][i], numTopWords))
            csvData[contentColName][i]=''.join(csvData[contentColName][i].split("', '")[0:numParagraphs])
            csvData[contentColName][i]=self.remove_character(csvData[contentColName][i])
        csvData['most_used_words']=self.listWords
        return csvData

    def export_json(self):
        data=self.format_data()
        jsonData=data.to_json(orient='records',force_ascii=False, indent=4)
        with open(self.jsonPath, 'w', encoding="utf-8") as outfile:
            outfile.write(jsonData)

