class Lexer:
  def __init__(self, code):
    self.code = code
    self.pos = -1
    self.char = None
    self.advance()
  def advance(self):
    self.pos += 1
    self.char = self.code[self.pos]
  # will finish this later or someone finish it if wants to
  # tokenize() function
  def makeTokens(self):
  	tokens = []