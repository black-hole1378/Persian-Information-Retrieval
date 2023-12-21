class Term:
   def __init__(self, term: str, term_id: int):
        self.term = term
        self.term_id = term_id
   
   def getTerm(self):
       return self.term
   
   def getTerm_ID(self):
       return self.term_id 
   
   def __lt__(self, other: object) -> bool:
        return self.term_id < other.term_id
    
   def __gt__(self, other: object) -> bool:
        return self.term_id > other.term_id
    
   
