# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Project: ALL Obfuscator
# Author: Night
# License: MIT
# Description: Python tool to obfuscate source code with two modes:
#              simple (1 layer) and ultra (multi-layer).
# -----------------------------------------------------------

import base64
import sys
import os
import random
import string

ASCII_ART = r'''
   ___   _    _ _     
  / _ \ | |  | | |    
 / /_\ \| |  | | |    
 |  _  || |/\| | |    
 | | | |\  /\  / |____
 \_| |_/ \/  \/\_____/
        A L L  🕶️        
'''

MENU = r'''
   ___   _    _ _     
  / _ \ | |  | | |    
 / /_\ \| |  | | |    
 |  _  || |/\| | |    
 | | | |\  /\  / |____
 \_| |_/ \/  \/\_____/
        A L L  🕶️        
    Python Obfuscator    
--------------------------
Commands:
▶ python main.py basic <file>
▶ python main.py extra  <file>
--------------------------
'''

def generate_random_var(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscate_once(source_code):
    encoded = base64.b64encode(source_code.encode('utf-8')).decode('utf-8')
    var_name = generate_random_var()
    return f'''
import base64 as {var_name}
exec({var_name}.b64decode("{encoded}").decode())
'''

def obfuscate_multiple(source_code, layers=5):
    code = source_code
    for _ in range(layers):
        code = obfuscate_once(code)
    return code

def write_output(original_path, content, suffix):
    base_name = os.path.basename(original_path)
    name, _ = os.path.splitext(base_name)
    output_file = f"{name}obf.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(ASCII_ART + "\n" + content)
    print(f"\n[✔] Obfuscated code written to: {output_file}")

def main():
    print("© 2024 - ALL Obfuscator | Created by Night | License: MIT")

    if len(sys.argv) == 1:
        print(MENU)
        return

    if len(sys.argv) != 3:
        print("[✘] Invalid usage. Try: python main.py simple <file> OR ultra <file>")
        return

    command = sys.argv[1]
    file_path = sys.argv[2]

    if not os.path.isfile(file_path):
        print(f"[✘] File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        original_code = f.read()

    if command == "basic":
        obfuscated = obfuscate_multiple(original_code, layers=5)
        write_output(file_path, obfuscated, "basic")

    elif command == "extra":
        obfuscated = obfuscate_multiple(original_code, layers=31)
        write_output(file_path, obfuscated, "ultra")

    else:
        print("[✘] Unknown command. Use 'simple' or 'ultra'.")

if __name__ == "__main__":
    main()
