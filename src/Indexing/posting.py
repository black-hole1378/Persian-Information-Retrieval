import bisect
class Posting: 
    def __init__(self,doc_id: int) -> None:
        self.doc_id = doc_id
        self.positions: int = list()
    
    def addPosition(self, postion: int) -> None:
        bisect.insort(self.positions, postion)
        
    def getDoc_ID(self) -> int:
        return self.doc_id 
    
    def getPosition(self) -> list:
        return self.positions
     
    def lenght(self) -> int:
        return len(self.positions)
    
    def __lt__(self, other: object) -> bool:
        return self.doc_id < other.doc_id

    def __gt__(self, other: object) -> bool:
        return self.doc_id > other.doc_id
    
            
        
    