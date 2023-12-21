from posting import Posting
import bisect
class PostingList:
    def __init__(self) -> None:
        self.frequency: int = 0
        self.posting_list: Posting = list()
    
    def addPosting(self, posting: Posting) -> None:
        bisect.insort(self.posting_list , posting)
        self.frequency += 1
         
    def get_posting_list(self) -> list:
        return self.posting_list

    
    def addPosition(self, position: int, docID: int) -> None:
        pass    
    
    def getFrequency(self) -> int:
        return self.frequency             