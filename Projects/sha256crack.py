from pwn import *
import sys

if len(sys.argv)!= 2:
    print("invalid args")
    print("with one arg"  )
    exit()

# for some reason this hash is not working > ECC7DCF5BC2D51EBC4D9A9C9108443E3E2B035C0E167594A63FF2FDE9A9CEA98
wanted_hash = sys.argv[1]
wanted_hash = wanted_hash.lower()
print(wanted_hash)
attempts = 0

with log.progress(f"Attempting to crack {wanted_hash}")as p:
    with open("c:\\Users\\work\\Documents\\Py 101\\Projects\\common.txt","r") as f:
        for pwd in f:
            pwd = pwd.strip("\n").encode('latin-1')
            pwd_hash = sha256sumhex(pwd)
            p.status(f"[{attempts}] {pwd.decode('latin-1')} == {pwd_hash}")
            if pwd_hash == wanted_hash:
                p.success(f"password found after {attempts} attempts {pwd.decode('latin-1')} hashes to {pwd_hash}")
                exit()
            attempts +=1
        p.failure("hash not found")