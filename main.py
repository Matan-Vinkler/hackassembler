from components.hackassembler import HackAssembler
from globals.strings import DEBUG_ARG

import sys

def main() -> int:
    if len(sys.argv) < 2:
        print(f"[-] Usage: {sys.argv[0]} <file.asm> [{DEBUG_ARG} (optinal)]")
        return -1
    
    debugFlag = len(sys.argv) == 3 and sys.argv[2] == DEBUG_ARG

    hackAsm = HackAssembler(sys.argv[1], debugFlag)

    hackAsm.firstPass()
    hackAsm.secondPass()

    return 0

if __name__ == "__main__":
    main()