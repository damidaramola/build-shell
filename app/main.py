import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    builtins = {"exit", "echo", "type"}
    
    while True:
        print("$ ", end="", flush=True)
        
        parts = input().strip().split()
        
        if not parts:
            continue
        
        command, *args = parts
        
        if command == "exit":
            sys.exit(0)
        
        elif command == "echo":
            print("".join(*args))
            # example: ["echo", "hello", "world"]
            
        elif command == "type":
            name = args[0]
            if name in builtins:
                print(f"{name} is a shell builtin")
            else:
                print(f"{name}: not found")
                    
        else:
            print(f"{command}: command not found")
            


if __name__ == "__main__":
    main()
