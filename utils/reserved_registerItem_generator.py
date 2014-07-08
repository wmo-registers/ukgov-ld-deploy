#!/usr/bin/python

# utility tool for automatically generating registerItem RDF (in TTL format) for  
# _reserved items_ defined within WMO code-tables
#
# example RDF:
#        []
#            a reg:RegisterItem ;
#            reg:definition [
#                reg:entity [
#                    a <http://codes.wmo.int/common/c-15/ae/runwayDeposits> ;
#                    rdfs:label "Reserved"@en ;
#                    dct:description "Reserved for future use."@en ;
#                ] ;
#            ] ;
#            reg:status reg:statusReserved ;
#            reg:notation 13 ;
#            bufr4-core:No 3050 ;
#            bufr4-core:FXY "020086" ;
#            bufr4-core:Status bufr4-core:statusOperational ;
#            .
#
# _reserved items_ may be generated for 'bufr4', 'grib2' or 'common'
# 'Status' is assumed to be 'statusOperational'
# each codeform has a {...}-core:No property
# if the codeform is 'bufr4', the property 'bufr4-core:FXY' shall be provided
#
# _reserved items_ will be generated in groups defined by a numeric range
# each _reserved item_ in the group will have the same {...}-core:No property
#

import re, sys, getopt

def main(argv): 
    usage = 'usage: reserved_registerItem_generator.py -s <start> -e <end> [-d <description>] -c <codeform> -n <no> [-f <fxy>] [-t <type>]\n'+ \
            '<start> and <end> define the range of integer values for which reserved items will be created\n'+ \
            '<description> provides the descriptive text used for the reserved item (optional; default \'Reserved\')\n' \
            '<codeform> shall be one of {bufr4|common|grib2} as appropriate for the target table\n'+ \
            '<no> is the line number from the CSV serialisation of the code-tables provided by WMO\n'+ \
            '<fxy> is required where <codeform> = bufr4; this is the 6-digit numerical identifier for the target table\n'+ \
            '<type> specifies the rdf:type of the item that is reserved (optional)'+'\r\n'
    supportedCodeforms = ['bufr4','common','grib2']
    start = -99
    end = -99
    description = 'Reserved'
    codeform = ''
    no = -99
    type = ''
    fxy = ''

    try:
        opts, args = getopt.getopt(argv,"hc:d:e:f:n:s:t:",["help","codeform=","description=","end=","fxy=","no=","start=","type="])
    except getopt.GetoptError:
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            sys.stdout.write(usage)
            sys.stdout.flush()
            sys.exit()
        elif opt in ("-c", "--codeform"):
            codeform = arg
            if codeform not in supportedCodeforms:
                sys.stdout.write('unsupported codeform\n'+'<codeform> shall be one of {bufr4|common|grib2}\r\n')
                sys.stdout.flush()
                sys.exit(2)
        elif opt in ("-e", "--end"):
            try:
                end = int(arg)
            except:
                sys.stdout.write('<end> must be an integer value ...\r\n')
                sys.stderr.write(usage)
                sys.stderr.flush()
                sys.exit(2)
        elif opt in ("-f", "--fxy"):
            fxy = arg
        elif opt in ("-n", "--no"):
            try:
                no = int(arg)
            except:
                sys.stdout.write('<no> must be an integer value ...\r\n')
                sys.stderr.write(usage)
                sys.stderr.flush()
                sys.exit(2)
        elif opt in ("-s", "--start"):
            try:
                start = int(arg)
            except:
                sys.stdout.write('<start> must be an integer value ...\r\n')
                sys.stderr.write(usage)
                sys.stderr.flush()
                sys.exit(2)
        elif opt in ("-t", "--type"):
            type = arg
        else:
            sys.stderr.write('Unrecognised argument ...'+'\r\n')
            sys.stderr.write(usage)
            sys.stderr.flush()
            sys.exit(2)
    
    if len(codeform) == 0 or no == -99 or start == -99 or end == -99:
        sys.stderr.write('Insufficient arguments provided. Found ('+str(len(opts))+') ...\r\n')
        sys.stderr.write('Input filename expected\r\n')
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
    
    if not end > start:
        sys.stderr.write('Invalid range: <start> must be less than <end> ...\r\n')
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
        
    if codeform == "bufr4" and len(fxy) == 0:
        sys.stderr.write('<fxy> must be defined where <codeform> is specified as \'bufr4\' ...\r\n')
        sys.stderr.write(usage)
        sys.stderr.flush()
        sys.exit(2)
    
    i = start
    while i<end+1:
        sys.stdout.write('[]\n')
        sys.stdout.write('    a reg:RegisterItem ;\n')
        sys.stdout.write('    reg:definition [\n')
        sys.stdout.write('        reg:entity [\n')
        if len(type):
            sys.stdout.write('            a '+type+' ;\n')
        sys.stdout.write('            rdfs:label "Reserved"@en ;\n')
        sys.stdout.write('            dct:description "'+description+'."@en ;\n')
        sys.stdout.write('        ] ;\n')
        sys.stdout.write('    ] ;\n')
        sys.stdout.write('    reg:status reg:statusReserved ;\n')
        sys.stdout.write('    reg:notation '+str(i)+' ;\n')
        sys.stdout.write('    '+codeform+'-core:No '+str(no)+' ;\n')
        if codeform == "bufr4":
            sys.stdout.write('    bufr4-core:FXY "'+fxy+'" ;\n')
        sys.stdout.write('    '+codeform+'-core:Status '+codeform+'-core:statusOperational ;\n')
        sys.stdout.write('    .\n')
        i+=1
    


if __name__ == "__main__":
    main(sys.argv[1:])
    sys.stdout.flush()

