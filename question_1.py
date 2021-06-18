"""
   write a program to replace all taboo words, saved in taboo file, 
   in all .txt files in the current directory with the corresponding 
   number of ‘*’, e.g. if there are 2 words in taboo: ‘bad’ and ‘worse’,
   then any word ‘bad’ and ‘worse’ in a txt file will be replaced by ‘***’
   and ‘*****’, and your program output the number of such replacements 
   after processing each file, if there are more than 
   5 taboo words in a file, the file is moved to the ‘trash’ folder.
"""
"""
design idea:
read the file and store them to a list
use binear search to find the taboo word
if the target is found, get the length of the taboo word and replace with '*'
that has equal length of the taboo word
set a counter to count the taboo word if it is more than 5 taboo word
file will move to the 'trash' folder
"""
import shutil, os

def read_file(path): # read each word in the file and return a list
   with open(path) as f:
      if not f.read(1):
         return "Empty file" # check if file is empty

      lst =  f.read().splitlines()

   return lst


def check_file_content(taboo_lst,lst,path): 
   # if file contain more than 5 taboo word, it will return false, 
   # else, return the file with taboo word replace by "*"
   taboo_count = 0
   for x,line in enumerate(lst): # iterate the lst
      # find all the tuboo word in a line and count 
      if taboo_count > 5: # if taboo word more than 5
         write_to_file(lst,path) 
         file_name = os.path.basename(path) # get the file name
         destination = "/Users/xin/Downloads/college_work/senior year /intern_pre/vscode_project/trash/" + file_name
         move_to_trash(path,destination) 
         return False
      for taboo in taboo_lst: # check the all the taboo word in the line 
         if taboo in line:
            lst[x] = line.replace(taboo,'*'*len(taboo)) # replace the taboo word with *
            taboo_count += line.count(taboo) # add the occurence of the taboo word

   write_to_file(lst,path)
   return True

def write_to_file(lst,path): # write to file
   with open(path,'w') as f:
      for line in lst:
         f.write("%s\n" % str(line))
   return f

def move_to_trash(source,destination): # move the file to trash folder
   shutil.move(source,destination)
   return True

path = "/Users/xin/Downloads/college_work/senior year /intern_pre/vscode_project/taboo.txt"
reg_path = "/Users/xin/Downloads/college_work/senior year /intern_pre/vscode_project/test_reg_file.txt"
trash_path3 = "/Users/xin/Downloads/college_work/senior year /intern_pre/vscode_project/test_trash_file.txt"

taboo_lst = read_file(path)
reg_file = read_file(reg_path)
trash_file = read_file(trash_path3)


print(check_file_content(taboo_lst,reg_file,reg_path))

print(check_file_content(taboo_lst,trash_file,trash_path3))
