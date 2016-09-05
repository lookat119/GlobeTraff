#!/usr/bin/python
'''
Function: Processes a 2-column proxy trace format and prints
          print out format: docid frequency, and size info
author:   melonli
date:     2016.9.3
'''

import sys
import os

def usage():
    print "Usage: %s <workload_file> <docs_file>" % sys.argv[0]

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    wf = sys.argv[1]
    df = sys.argv[2]
    items = {}
    min_iid = 18446744073709551616
    max_iid = 0
    with open(wf, 'r') as w:
        buf = w.readline()
        while(buf != ""):
            buf = buf.strip()
            (iid, isize) = buf.split(" ")
            iid = int(iid)
            if min_iid > iid: min_iid = iid
            if max_iid < iid: max_iid = iid
            if items.has_key(iid):
                items[iid][0] = items[iid][0] + 1
            else:
                items[iid] = [1, isize]
            buf = w.readline()
   
   
    print min_iid
    with open(df, 'w') as d:
        for i in xrange(min_iid, max_iid+1, 1):
            if not items.has_key(i): continue
            buf = items[i]
            s= '%d\t%d\t%s\t1\n' % (i, buf[0], buf[1])
            d.write(s)
            

if __name__ == "__main__":
    sys.exit(main())
