#!/usr/bin/env python

import sys, re #Imports the necessary library 
from argparse import ArgumentParser # to import the function

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') #Makes an object (parser) with the description 
parser.add_argument("-s", "--seq", type = str, required = True, help ="Input sequence") #To create input sequence variable and motif
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1: #To check the number of arguments
   parser.print_help()
   sys.exit(1)

args = parser.parse_args() 

#To convert the input to upper-case 
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq): #Is there any T?
        print ('The sequence is DNA') #If yes, sequence is DNA
    elif re.search('U', args.seq): #Is there any U?
        print ('The sequence is RNA') #If yes, sequence is RNA
    else:
        print ('The sequence can be DNA or RNA') #If not either one, sequence can be DNA or RNA
else:
    print ('The sequence is not DNA nor RNA')
   
#To find specific sequences or motifs
if args.motif:
   args.motif = args.motif.upper() #To turn it to uppercase
   print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
   if re.search(args.motif, args.seq): #Is there the motif? 
       print("FOUND") #If yes, it prints "found"
   else:
       print("NOT FOUND") #If no, it prints "not found"      
