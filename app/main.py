import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    commands = {"exit":sys.exit, "echo": print}
    while True:
        print("$ ", end="")
        
        command, *args = input().strip().split()
        
        if command in commands:
            commands[command](*args)
        else:
            print(f"{command}: command not found")
            


if __name__ == "__main__":
    main()
