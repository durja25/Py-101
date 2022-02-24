from pwn import *

# The DeBraun cyclic pattern. It is important to find offsets for buffer overflows. We can call
print(cyclic(50))
# it directly using pwn

# We can also find the cyclic pattern of a string using cyclic_find
print(cyclic_find("laaa"))

# We can directly work with assembly using this command
print(shellcraft.sh())
# We can have the hexdump of the shellcode(assembly) in asm using this command
print(hexdump(asm(shellcraft.sh())))

# # We can start a process using this command
# p = process("/bin/sh")
# # We can send this line to our started process
# p.sendline("echo Hello!;")
# # We can make the process we started be interactive using this command
# p.interactive()

# # We can also start a process on a remote workstation
# r = remote("127.0.0.1", 1337)
# # We can send a line on their shell using this command
# r.sendline("Hell!")
# # We can start an interactive session for the remote machine
# r.interactive()
#  # We can close the interactive session using this command
# r.close()

# We can pack data using this command. The numbers can effectively change though
print(p32(0x13371337))
# We can unpack the data in the above line using this process. We specifically
# ask to print it in hex because the input in the above line was in hex
print(hex(u32(p32(0x13371337))))

# We can load files this way using pwntools.
# ELF stands for Executable and Linkable Format
l = ELF('/bin/bash')
# We can look at the hex address of our program using this command
print(hex(l.address))
# We can also see the entry point of the program
print(hex(l.entry))

# We can know the address of a specific symbol from the global offset table
print(hex(l.got['write']))
# We can also grab information about a specific sample from the
# procedure linkage table
print(hex(l.plt['write']))

# We are searching for addresses where we can find the /bin/sh stream
# with a null terminator
for address in l.search(b'/bin/sh\x00'):
    print(hex(address))

# We can search for a specific address in the ELF which isn't represented as a stream
print(hex(next(l.search(asm('jmp esp')))))

# The ROP function makes it much easier on us to find this streams and addresses
r = ROP(l)
# This lets us search for specific gadgets in the ELF. This time, we're searching for rbx.
print(r.rbx)

# We have access to hashing, encryption and encoding functions with pwntools. XOR is one of them.
print(xor("A", "B"))
# We can make sure of the above result this way
print(xor(xor("A", "B"), "A"))

# We have access to base64 encoding in pwntools.
print(b64e(b"test"))
# We have access to base64 decoding as well.
print(b64d(b"dGVzdA=="))

# We also have md5 sums
print(md5sumhex(b"hello"))

# We have access to sha1 as well. Use this with hex as it will be confusing otherwise.
print(sha1sumhex(b"hello"))

# We can print the bits for characters and strings
print(bits(b'a'))
# We can change bits to their corresponding characters or strings.
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))