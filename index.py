import time
import random
class FileElement:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent

class Folder(FileElement):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = {}
        self.created = time.ctime()
        self.type = "folder"
        self.size = 0

class File(FileElement):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.size = random.randint(1,10)
        self.created = time.ctime()
        self.type = "file"



class FileManager:
    def __init__(self):
        self.root = Folder("root",None)
        self.current = self.root

    def FolderCreater(self,name):
        if (name == "root"):
            print("choose any other name other than root")
            return
        if (name in self.current.children):
            print(f"{name} already exists in current directory({self.current.name})")
            return 
        if(self.current.type=="file"):
            print(f"{name} is not a folder!")
            return
        newFolder = Folder(name,self.current)
        self.current.children[name] = newFolder
        newFolder.parent = self.current
    
        print(f"Created Folder '{name}' in current directory({self.current.name})")

    def FileCreater(self,name):
        if (name=="root"):
            print("choose any other name other than root")
            return
        if (name in self.current.children):
            print(f"{name} already exists in current directory({self.current.name})")
            return 
        if(self.current.type=="file"):
            print(f"{name} is not a folder!")
            return
        newFile = File(name,self.current)
        self.current.children[name] = newFile
        newFile.parent = self.current
        print(f"Created File '{name}' in current directory({self.current.name})")

    def CurrentDirectory(self):
        path=[]
        tempself = self.current
        path.append(self.current.name)
        while(tempself.parent!=None):
            tempself = tempself.parent
            path.append(tempself.name)
            print("Current Directory: ",end="")
        for i in range(len(path)-1,-1,-1):
            print(path[i],end='/')
        print()


    def list(self):
        print(f"{self.current.name}:")
        print("date \t\t\t\t name")
        for i in self.current.children:
            print(f"{self.current.children[i].created} \t {i}")
    def info(self,name):
        if (name in self.current.children):
             print("date \t\t\t\t name  size")
             print(f"{self.current.children[name].created} \t {name} \t{self.current.children[name].size}")
        else:
            print(f"{name} doesnt exist")
    
    def cd(self,node):
        if(node ==".."):
            if(self.current =="root"):
                print("Current directory is root. Cannot go back any further")
                return 
            self.current = self.current.parent
        
        elif (node in self.current.children):
            if (self.current.children[node].type=="file"):
                print("Cannot cd into file")
                return
            self.current = self.current.children[node]

        else:
            print(f"{node} doesn't exist in current directory({self.current.name})")

        self.CurrentDirectory()

    def delete(self,name):
        if (name in self.current.children):
            del self.current.children[name]
            
        else:
            print(f"{name} doesn't exist in current directory({self.current.name})")
    def rename(self,old, final):
        if (old not in self.current.children):
                        print(f"{old} doesnt exist")
                        
        else:
            temp = self.current.children[old]
            self.delete(old)
            self.current.children[final] = temp
            print(f"{old} renamed to {final}")
    def resolve_path(self, path):
        if path.startswith("/"):
            node = self.root
            parts = path.strip("/").split("/")
        else:
            node = self.current
            parts = path.split("/")

        for part in parts:

            if part == "" or part == ".":
                continue

            if part == "..":
                if node.parent:
                    node = node.parent
                continue

            node = node.children.get(part)

            if not node:
                return None

        return node

    def tree(self, node=None, prefix=""):

        if node is None:
            node = self.root
            print(node.name)

        children = list(node.children.values())

        for i, child in enumerate(children):

            connector = "└── " if i == len(children) - 1 else "├── "

            print(prefix + connector + child.name)

            if isinstance(child, Folder):

                extension = "    " if i == len(children) - 1 else "│   "
                self.tree(child, prefix + extension)


class App:
    def __init__(self):
        self.fm = FileManager()
        self.commands = {
            "list": self.fm.list,
            "pwd": self.fm.CurrentDirectory
        }
    def execute(self):
        while(True):
            command = input()
            if (command.lower().strip()=="exit"):
                break
            instruction = command.split()
            if (command==""):
                print("Enter valid command")
                continue
            if (instruction[0]=="app"):
                if (instruction[1]=="folders"):
                    if ("," in command):
                        
                        parent = instruction[2].strip(",")
                        folders = instruction[4:]
                        if (parent in self.fm.current.children):
                            self.fm.current = self.fm.current.children[parent]
                            for foldername in folders:
                                self.fm.FolderCreater(foldername)
                        else:
                            print(f"{parent} doesn't exist")
                    else:
                        folders = instruction[2:]
                        for foldername in folders:
                            self.fm.FolderCreater(foldername)
                    continue
                
                elif (instruction[1] == "files"):
                    files = instruction[2:]
                    for filename in files:
                        self.fm.FileCreater(filename)
                    
                    continue

                elif (instruction[1] in self.commands):
                    self.commands[instruction[1]]()
                    continue

                elif (instruction[1] == "delete"):
                    toDelete = instruction[2:]
                    for element in toDelete:
                        self.fm.delete(element)
                        print(f"{element} deleted")
                    continue
                elif (instruction[1]=="represent"):
                    self.fm.tree()
                    continue
                elif (instruction[1] == "cd"):
                    self.fm.cd(instruction[2])
                    continue
                
                elif (instruction[1] == "rename"):
                    original = instruction[2]
                    final = instruction[3]
                    self.fm.rename(original,final)
                    continue
                
                elif (instruction[1] == "info"):
                    filename = instruction[2]
                    self.fm.info(filename)

                elif (instruction[1] == "copy" or instruction[1] == "move"):
                    source = instruction[2]
                    destination = instruction[3]
                    if (source == None or destination == None ):
                        print("specify valid source and destination")

                    else:
                        sourcenode = self.fm.resolve_path(source)
                        destinationnode = self.fm.resolve_path(destination) 
                        if (sourcenode==None or destinationnode==None):
                            print("Couldn't find directory")
                            continue
                        destinationnode.children[sourcenode.name] = sourcenode
                        if (instruction[1]=="copy"):
                            print(f"Successfuly copied {source} to {destination.name} ")
                
                        else:
                            self.fm.current = sourcenode.parent
                            self.fm.delete(sourcenode.name)
                            print(f"Successfuly moved {source} to {destinationnode.name} ")
                    
                    self.fm.CurrentDirectory()
                    print()

                    continue
                else:
                    print("Invalid command!")
                    continue

            else:
                print("Invalid command!")  
                
                

app = App()
app.execute()
app.fm.ls()
app.fm.CurrentDirectory()