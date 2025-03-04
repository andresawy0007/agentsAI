from  abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
import os, json
os.environ['OPENAI_API_KEY'] = ""

class iNode(ABC):

    _instance = None

    def getOpenAIInstance(self):
        if iNode._instance is None:
            iNode._instance = ChatOpenAI(temperature=0.4)
        return iNode._instance
    
    def buildJsonRespond(self, data):
        return json.loads(data);

    @abstractmethod 
    def run (self, state): 
        pass;