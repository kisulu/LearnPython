import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


try:
    os.makedirs("tree/python")
    os.chdir("tree")
    os.makedirs("./cpp/other_courses/python")
    os.makedirs("./c/other_courses/python")

except FileExistsError:
    directory_searcher = DirectorySearcher()
    directory_searcher.find("./tree", "python")




##    def find(path, dir):
##        # Ensure the provided path is valid
##        if not os.path.isdir(path):
##            print(f"The path '{path}' is not a valid directory.")
##           return
##
##        # Traverse the directory tree
##        for root, dirs, files in os.walk(path):
##            if dir in dirs:
##                # Print the absolute path of the found directory
##                print(os.path.abspath(os.path.join(root, dir)))
##
##    # Example usage:
##    find('./tree', "tree")
##   

