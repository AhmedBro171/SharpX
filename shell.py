# Edited by happen3 to integrate the modules.

import opcodeParser

while true:
  userinput = input("> ")
  result = opcodeParser.parse_opcode(userinput)
