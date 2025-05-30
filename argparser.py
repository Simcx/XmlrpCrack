import argparse

def argumentHandler(args):
    parser = argparse.ArgumentParser(
        prog = 'XmlrpCrack',
        usage = 'WordPress Password Cracker')
    
    parser.add_argument('USERNAME', help='username you wish to crack password for')
    parser.add_argument('PASSLIST', type=argparse.FileType('r'), help='wordlist you wish to use in dictionary attack')
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), help='outputs to a given file')
    
    parsedArgs = parser.parse_args(args)
    
    return parsedArgs