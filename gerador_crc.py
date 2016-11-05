# Cyclic redundancy check
# Autor: Leonardo E. Wajnsztok

def divisao_modulo_dois(dividendo, divisor):
	print "Divisao modulo 2"
	print bin(dividendo), "|__", bin(divisor)

	quociente = 0
	k = dividendo.bit_length()
	r = divisor.bit_length()
	aux = k - r

	# Separa-se um numero de algarismos do dividendo igual ao do divisor
	resto = dividendo >> (aux)

	while aux > -1:
		# Conta-se o numero de bits 1 separado do dividendo
		num_bit = resto.bit_length()

		# Coloca-se um bit 1 no quociente sempre que o numero de bits 
		# separados e contados do dividendo for igual ao do divisor.
		# Quando esse numero eh menor do que o do divisor, o bit 
		# colocado no quociente eh o zero.

		quociente <<= 1
		if num_bit == r:
			quociente |= 1
			resto ^= divisor
			print "%s%9s%s" %((k - r - aux) * ' ', bin(divisor), (aux) * '|')
		else:
			print "%s%s%s" % ((k - r - aux) * ' ', "0b0000000", (aux) * '|')
		print  "%s%s%s" % ((k - r - aux) * ' ',"---------", (aux) * '|')

		aux -= 1
		if aux > -1:
			resto  = ((resto << 1) | ((dividendo >> aux) & 1))
		print "%s%9s%s" % ((k - r - aux) * ' ', bin(resto), (aux) * '|')

	print "\nQuociente:", bin(quociente)
	print "Resto:", bin(resto)
	return (quociente, resto)


def gerador_crc(mensagem, polinomio):

	k = mensagem.bit_length()
	r = polinomio.bit_length()

	mensagem_com_zeros = mensagem << (r - 1)
	quociente, fcs = divisao_modulo_dois(mensagem_com_zeros, polinomio)
	mensagem_transmitida = mensagem_com_zeros ^ fcs

	return (mensagem_transmitida, fcs)


if __name__ == '__main__':
	
	mensagem = 0b11001101001101010010111010010110
	polinomio = 0b1110011

	mensagem_transmitida, fcs = gerador_crc(mensagem, polinomio)
	
	print "\nFCS:", bin(fcs)
	print "Mensagem transmitida:", bin(mensagem_transmitida)


	print "Verificacao do CRC na recepcao:"
	_, resto = divisao_modulo_dois(mensagem_transmitida, polinomio)
	print "Transmissao com sucesso!" if resto == 0 else "Falha na transmissao."