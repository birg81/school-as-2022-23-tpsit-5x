from encDecMsg import encode, decode
import sys

if len(sys.argv) > 1:
	msg = ' '.join(sys.argv[1:])
else:
	msg = input('Insert your message: ').strip()

print(
f'''
* msg:	{msg}
* enc:	{encode(msg)}
* dec:	{decode(encode(msg))}
'''
)