import token

class Lexer:
  def __init__(self, code):
    self.code = code
    self.pos = -1
    self.char = None
    self.advance()
  def advance(self):
    self.pos += 1
    self.char = self.code[self.pos]
  def makeTokens(self):
  	tokens = []

  	while self.char != None:
  		if self.char == "+":
  			tokens.push(token.Token(token.TokenType.plus))
  		if self.char == "-":
  			tokens.push(token.Token(token.TokenType.minus))
  		if self.char == "*":
  			tokens.push(token.Token(token.TokenType.multiply))
  		if self.char == "/":
  			tokens.push(token.Token(token.TokenType.divide))

  	return tokens