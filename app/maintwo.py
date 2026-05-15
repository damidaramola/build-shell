import sys
import os
import subprocess

class Shell:
    def __init__(self):
        self.builtins = {"exit", "echo", "type"}
        self.path_dirs  = os.environ['PATH'].split(os.pathsep)
    
    def check_path(self, cmnd):
        
        for dir in self.path_dirs:
            full_path = os.path.join(dir, cmnd)
            
            if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                print(f"{cmnd} is {full_path}")
                
                
                return full_path
        return None 
                
    
    def exit(self):
        sys.exit(0)
        
    def echo(self,args):
        print(" ".join(args))
        
    def type(self,args):
        name= args[0]
        if name in self.builtins:
            print(f"{name} is a shell builtin")
        else:
            result = self.check_path(name)
            if result is None:
                print(f"{name}: command not found")
            
    
def main():
    shell = Shell()
    while True:
        print("$ ", end="", flush=True)
        
        parts = input().strip().split()
        
        if not parts:
            continue
        
        command, *args = parts
        
        if command == 'exit':
            shell.exit()
        elif command == 'echo':
            shell.echo(args)
        elif command == 'type':
            shell.type(args)
        else:
            full_path = shell.check_path(command)
            if full_path:
                process = subprocess.Popen([command, *args], executable=full_path)
                process.wait()
                
            else:
                print(f"{command}: command not found")
                
    
                        
if __name__ == "__main__":
    main()