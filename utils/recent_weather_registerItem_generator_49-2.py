#!/usr/bin/python

# utility tool for automatically generating registerItem RDF (in TTL format) for terms
# within /49-2/AerodromeRecentWeather register based on list provided by ICAO AMOFSG/10
# @//src/weather-codes/recent-weather-codes-REww.txt 
#
# example string: 
#        'REBLSN,"Blowing snow"'
# example RDF:
#        []
#            a reg:RegisterItem ;
#            reg:definition
#                [ reg:entity <http://codes.wmo.int/306/4678/BLSN> ] ;
#            reg:status reg:statusStable ;
#            reg:notation "REBLSN" ;
#            .
#        <http://codes.wmo.int/306/4678/BLSN>
#            a skos:Concept ;
#            rdfs:label "Blowing snow"@en ;
#            .
#

import re, sys, getopt

class Tokeniser:
    """string tokeniser for comma-delimited txt files with embedded quoted text fields"""
    def __init__(self, inputString=None):
        s = inputString
        self.list=[]
        i=0

        while i<len(s):
            if s[i]=='"':
                try:
                    j=s.index('"',i+1)
                    sub=s[i+1:j]
                except ValueError:
                    break
                inc=2
            else:
                try:
                    j=s.index(',',i)
                    sub=s[i:j]
                except ValueError:
                    break
                inc=1

            self.list.append(sub)
            i=j+inc

def main(argv): 
    usage= 'usage: recent_weather_registerItem_generator_49-2.py -i <inputfile>'+'\r\n'
    inputFileName = ''
# set indexes to match columns
    index_Code = 0
    index_Description = 1

    try:
        opts, args = getopt.getopt(argv,"hi:",["help","ifile="])
    except getopt.GetoptError:
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            sys.stdout.write(usage)
            sys.stdout.flush()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileName = arg
        else:
            sys.stderr.write('Unrecognised argument ...'+'\r\n')
            sys.stderr.write(usage)
            sys.stderr.flush()
            sys.exit(2)
    
    if len(inputFileName) == 0:
        sys.stderr.write('Insufficient arguments provided. Found ('+str(len(opts))+') ...\r\n')
        sys.stderr.write('Input filename expected\r\n')
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
    
    with open(inputFileName, 'r') as infile:
# wite prefix statements
        sys.stdout.write('@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .\n')
        sys.stdout.write('@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .\n')
        sys.stdout.write('@prefix dct:     <http://purl.org/dc/terms/> .\n')
        sys.stdout.write('@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .\n')
        sys.stdout.write('@prefix reg:     <http://purl.org/linked-data/registry#> .\n')
        sys.stdout.write('@prefix ldp:     <http://www.w3.org/ns/ldp#> .\n')
        sys.stdout.write('@prefix foaf:    <http://xmlns.com/foaf/0.1/> .\n')
        sys.stdout.write('\n')
        
        for line in infile: 
            list = Tokeniser(line).list
            if list:
                code = list[index_Code]
                description = list[index_Description]
                sys.stdout.write('[]\n')
                sys.stdout.write('    a reg:RegisterItem ;\n')
                sys.stdout.write('    reg:definition\n')
                sys.stdout.write('        [ reg:entity <http://codes.wmo.int/306/4678/'+code[2:len(code)]+'> ] ;\n')
                sys.stdout.write('    reg:status reg:statusStable ;\n')
                sys.stdout.write('    reg:notation "'+code+'" ;\n')
                sys.stdout.write('.\n')
                sys.stdout.write('<http://codes.wmo.int/306/4678/'+code[2:len(code)]+'>\n')
                sys.stdout.write('    a skos:Concept ;\n')
                sys.stdout.write('    rdfs:label "'+description+'"@en ;\n')
                sys.stdout.write('.\n')                
            else:
                sys.stdout.flush()
                sys.exit()
                

if __name__ == "__main__":
    main(sys.argv[1:])
    sys.stdout.flush()

