# XmlrpCrack
Created by @Simcx

For professional and ethical use ONLY. Any malicious behaviour is highly discouraged and can cause you serious penalties.

XmlrpCrack use case: password cracking with xmlrpc's system.multicall function

## Requirements

> Target must be using WordPress with xmlrpc.php enabled.
    You can check this by going to http://[EXAMPLE_SITE]/xmlrpc.php.
    You'll see a "XML-RPC server accepts POST requests only."

> You must know the username of the WordPress account you want to do this with.
  The response is a more generic error message so you have to enumerate the username somehow.

## How it Works

> XmlrpCrack takes a required username and a password wordlist.

> XmlrpCrack will generate a payload by adding a new function call within the system.multicall function for however many words are in your password wordlist.

> As of right now, it only outputs to standard output or to a file of your choice. Eventually, it will send a POST request to the specified URL.
  This will be an optional task specified by you, in which not specifying so AND not outputting it to a file will just print it to standard output.
