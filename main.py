"""
Reflector : A
Rotors : I- II - III
Plugboard : A-R, G-K, O-X
Message : A => X
"""

from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector

I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')

KB = Keyboard()
PB = Plugboard(['AR', 'GK', 'OX'])

letter = 'A'
signal = KB.forward(letter)
signal = PB.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = PB.backward(signal)
letter = KB.backward(signal)
print(letter)