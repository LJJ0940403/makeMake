import sys
import os

if len(sys.argv) < 2:
    print('Usage: python3 pmake.py <exe name>')
    exit(0)

exe_name = sys.argv[1]
folder = os.path.dirname(os.path.abspath(__file__))

src_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.cpp')]
header_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.h')]

src_files = [os.path.basename(i) for i in src_files]
header_files = [os.path.basename(i) for i in header_files]
obj_files = [file_name.replace('.cpp', '.o') for file_name in src_files]

print(f"header file: {' '.join(header_files)}")
print(f"source file: {' '.join(src_files)}")

with open("Makefile", 'w') as f:
    f.write(f"all: {exe_name}\n\n")
    
    f.write(f"{exe_name}: {' '.join(obj_files)}\n")
    f.write(f"\tg++  {' '.join(obj_files)} -o {exe_name}\n\n")
    
    for i in range(len(src_files)):
        content = f"{obj_files[i]}: {src_files[i]}\n\tg++ -c {src_files[i]}\n\n"
        f.write(content)
    
    f.write(f"debug: {' '.join(src_files)} {exe_name}\n")
    for i in range(len(src_files)):
        content = f"\tg++ -c -D debug {src_files[i]}\n"
        f.write(content)    
    f.write(f"\tg++ -D debug {' '.join(obj_files)} -o {exe_name}\n\n")
            
    f.write("clean:\n\trm *.o -f")
