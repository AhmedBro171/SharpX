import randomGen

def parse_opcode(opcode):
	# Here we check the opcode from a list.
	opcodes = ['stdout.print', 'stdin.input', 'random']
	code = opcode.split()[0]
	argument = opcode.split()[1]
	
	for opc in opcodes:
		if code == opc:
			if opc == 'stdout.print':
				print(argument)
			if opc == 'stdin.input':
				inp = input(argument)
				return inp
			if opc == 'random':
				return randomGen.Generate()
			
