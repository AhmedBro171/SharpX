import randomGen

def parse_opcode(opcode):
	# Here we check the opcode from a list.
	opcodes = ['stdout.print', 'stdin.input', 'random']
	code = opcode.split()[0]
	argument = opcode.split()[1]
	
	c = 0
	
	for opc in opcodes:
		c =+ 1
		if code == opc:
			if opc == opcodes[c]:
				print(argument)
			if opc == opcodes[c]:
				inp = input(argument)
				return inp
			if opc == opcodes[c]:
				return randomGen.Generate()
			
