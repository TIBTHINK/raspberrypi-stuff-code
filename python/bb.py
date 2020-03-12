from os import system as cmd
import os

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo !!' then run the script.\nExiting.")

print("###WARNING###")
print("this code will delete everything in the repo if ran")
print("it is recomended that you use curl to run this command to leave no edvidence")

a = input("are you sure you want to do this? (type yes if you are sure): ")

if "yes" in a:
    while True:
        cmd("git rm -rf *")
        cmd("git commit -m 'bye bye love'")
        cmd("git push")
        print("have a good day")
        exit()
    else:
        print("alright see you when you need to do this")
        exit()
