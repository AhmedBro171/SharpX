# i hope i won't get addicted to python while writing this ig lol

TokenType_plus = "plus"
TokenType_minus = "minus"
TokenType_multiply = "multiply"
TokenType_divide = "divide"

class Token:
  def __init__(self, type, value=None):
    self.type = type
    self.value = value
