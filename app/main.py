import sys
import os
import subprocess

def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = {"exit", "echo", "type"}
    

    while True:
        print("$ ", end="", flush=True)
        
        path_dirs  = os.environ['PATH'].split(os.pathsep)
        
        parts = input().strip().split()
        
        if not parts:
            continue
        
        command, *args = parts
        
        if command == "exit":
            sys.exit(0)
        
        elif command == "echo":
            print(" ".join(args))
            # example: ["echo", "hello", "world"]
            
        elif command == "type":
            
            name = args[0]
            if name in builtins:
                print(f"{name} is a shell builtin")
                     
            else:
                found = False
                for directory in path_dirs:
                    full_path = os.path.join(directory,name)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{name} is {full_path}")
                        found = True
                        break
                        
                if not found:
                    print(f"{name}: not found")
        else:
                for directory in path_dirs:
                    full_path = os.path.join(directory,command)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        result = subprocess.run([command, *args])
                        print(result.stdout)
                    else:
                        print(f"{command}: command not found")
                    
        
            


if __name__ == "__main__":
    main()
