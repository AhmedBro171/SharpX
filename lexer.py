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
  		elif self.char == "-":
  			tokens.push(token.Token(token.TokenType.minus))
  		elif self.char == "*":
  			tokens.push(token.Token(token.TokenType.multiply))
  		elif self.char == "/":
  			tokens.push(token.Token(token.TokenType.divide))
      else:
        char = self.char
        self.advance()
        return None, UndefinedCharError("'" + char + "'")

  	return tokens, None