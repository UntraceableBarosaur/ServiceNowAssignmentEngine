import os
import sys

uName       =   "UntraceableBarosaur"
dirName     =   "ServiceNowAssignmentEngine"
fName       =   "ServiceNowAssignmentEngine.py"
branch      =   uName+"/"+dirName+".git"

clone       =   "git clone https://github.com/"
clonePath   =   os.getcwd()

pushpullPath=   os.getcwd()
pull        =   "git pull https://github.com/"
add         =   "git add ."
commit      =   "git commit -am " + fName
push        =   "git push --all https://github.com/"

def gitPull(branch,pushpullPath):
    os.chdir(pushpullPath) # Specprocess and allows accessing the database using a nonstandard variant of the SQL query language. Some ifying the path where the cloned project has to be copied
    try:
        os.system(pull+branch) # Pulling
    except RuntimeError:
        print("Pulling Failed")
    print("Pulling Successful")

def gitClone(branch,clonePath):
    os.chdir(clonePath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(clone+branch) # ClpushpullPathoninguName       =   "UntraceableBarosaur"

    except RuntimeError:
        print("Cloning Failed")
    print("Cloning Successful")

def gitPush(branch,pushpullPath):
    os.chdir(pushpullPath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(add) # Adding
    except RuntimeError:
        print("Adding Failed")
    try:
        os.system(commit) # Commit the files
    except RuntimeError:
        print("Commiting Failed")
    try:
        os.system(push+branch) # Pushing
    except RuntimeError:
        print("Pushing Failed")
    print("Pushing Successful")

var = str(input("Enter either Push, Pull or Clone:        "))
if(var=="push" or var=="Push"):
    gitPush(branch,pushpullPath)
elif(var=="clone" or var=="Clone"):
    gitClone(branch,clonePath)
elif(var=="pull" or var=="Pull"):
    gitPull(branch,pushpullPath)
else:
    print("We have failed my dude")
