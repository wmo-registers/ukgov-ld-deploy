#!/usr/bin/python

# pragma tool for manipulating BUFRCREX CodeFlag .txt file ...
# i)  lines with CodeFigure matching the pattern '{m}-{n}' _AND_ EntryName_en beginning 
#     with either 'Reserved' or 'Not used' will be expanded out
# ii) lines with CodeFigure beginning with 'All ' (e.g. the final term in a Flag-table) 
#     have the 'All ' string removed
#
# -e <fxy> selects a specific target Element from the input file
# -x <fxy> excludes a specific target Element from the input file (e.g. 001036 "Agency 
#          in charge of operating the observing platform" which expands to thousands of 
#          entries!
#

import re, sys, getopt

class Tokeniser:
# example string: '3041.00,"020086","Runway deposits","1","Damp",,,,"Operational"'
    """string tokeniser for WMO Code-table txt files"""
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
    usage= 'usage: pragma.py -i <inputfile> [-e <fxy>] [-x <fxy>]'+'\r\n'
    inputFileName = ''
# set {fxy} to empty string - everything matches by default
    fxy = ''
# set {fxy_exclude} to imposible string - nothing matches by default
    fxy_exclude = '000000'
# set indexes to match columns
    index_No = 0
    index_FXY = 1
    index_ElementName_en = 2 
    index_CodeFigure = 3
    index_EntryName_en = 4
    index_EntryName_sub1_en = 5
    index_EntryName_sub2_en = 6
    index_Note_en = 7
    index_Status = 8

    try:
        opts, args = getopt.getopt(argv,"hi:e:x:",["help","ifile=","element=","exclude="])
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
        elif opt in ("-e", "--element"):
            fxy = arg
        elif opt in ("-x", "--exclude"):
            fxy_exclude = arg
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
    
    codeFigureGroupPattern = re.compile('^([\d]+)-([\d]+)$')
    reservedEntryPattern = re.compile('^Reserved')
    notUsedPattern = re.compile('^Not used')
    fxyPattern = re.compile('^'+fxy+'.*$')
    fxyExcludePattern = re.compile('^'+fxy_exclude+'.*$')
    allFlagsPattern = re.compile('^All ([\d]+)$')
    
    with open(inputFileName, 'r') as infile:
        for line in infile: 
            list = Tokeniser(line).list
            if fxyExcludePattern.match(list[index_FXY]):
                continue
            elif fxyPattern.match(list[index_FXY]):
                codeFigureAllFlags = allFlagsPattern.match(list[index_CodeFigure])
                if reservedEntryPattern.match(list[index_EntryName_en]) or notUsedPattern.match(list[index_EntryName_en]):
                    codeFigureGroup = codeFigureGroupPattern.match(list[index_CodeFigure])
                    if codeFigureGroup:
                        for i in range(int(codeFigureGroup.group(1)), int(codeFigureGroup.group(2))+1):
                            sys.stdout.write('\t'.join([list[index_No],list[index_FXY],list[index_ElementName_en],str(i),list[index_EntryName_en],list[index_EntryName_sub1_en],list[index_EntryName_sub2_en],list[index_Note_en],list[index_Status]])+'\n')
                elif codeFigureAllFlags:
                    sys.stdout.write('\t'.join([list[index_No],list[index_FXY],list[index_ElementName_en],codeFigureAllFlags.group(1),list[index_EntryName_en],list[index_EntryName_sub1_en],list[index_EntryName_sub2_en],list[index_Note_en],list[index_Status]])+'\n')
                else:
                    sys.stdout.write('\t'.join([list[index_No],list[index_FXY],list[index_ElementName_en],list[index_CodeFigure],list[index_EntryName_en],list[index_EntryName_sub1_en],list[index_EntryName_sub2_en],list[index_Note_en],list[index_Status]])+'\n')
     

if __name__ == "__main__":
    main(sys.argv[1:])
    sys.stdout.flush()

