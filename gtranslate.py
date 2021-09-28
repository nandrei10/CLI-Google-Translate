#!/usr/bin/env python

import getopt
import sys
import time

from googletrans import Translator
from threading import Thread

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "f:l:")
    except getopt.GetoptError:
        print ('Usage: python gtranslate.py -f <filename> -l <lang>')
        print ('Parameters:')
        print ('    -f <filename>: path to input filename to be translated')
        print ('    -l <lang>: output language, can be one of "en", "it" or "de"')
        sys.exit(2)
        
    if len(opts) == 0 or len(opts) > 2:
        print ('Usage: python gtranslate.py -f <filename> -l <lang>')
        print ('Parameters:')
        print ('    -f <filename>: path to input filename to be translated')
        print ('    -l <lang>: output language, can be one of "en", "it" or "de"')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: python gtranslate.py -f <filename> -l <lang>')
            print ('Parameters:')
            print ('    -f <filename>: path to input filename to be translated')
            print ('    -l <lang>: output language, can be one of "en", "it" or "de"')
            sys.exit()
        elif opt == '-f':
            input_file = arg
        elif opt == '-l':
            language = arg

    f = open(input_file, 'r')
    print ('Translating, please wait…')
    for line in f:
        T = Thread(target=gtranslate(line, language))
        T.setDaemon(True)
        T.start()
        
        # Sleep here to limit the amount of req/s
        time.sleep(0.1)
    
def gtranslate(line, language):
    translator = Translator()  
    result = translator.translate(line, dest=language)
    print (result.text)

if __name__ == "__main__":
    # run the main program
    main(sys.argv[1:])
