import json
from subprocess import Popen, PIPE

#refered to http://stackoverflow.com/questions/8856032/reading-binary-plist-files-with-python

def bplist_to_dictionary(filename):
    "Pipe the binary plist through plutil and parse the JSON output"
    with open(filename, "rb") as f:
        content = f.read()
    
    #some key cannot be directly convert from bplist to json (such as <data>)
    #so first convert bplist to plist, then replace 'DATA' with 'STRING', and do convert plist to json
    args = ["plutil", "-convert", "xml1", "-o", "-", "--", "-"]
    p = Popen(args, stdin=PIPE, stdout=PIPE)
    p.stdin.write(content)
    out, err = p.communicate()

    args2 = ["plutil", "-convert", "json", "-o", "-", "--", "-"]
    p2 = Popen(args2, stdin=PIPE, stdout=PIPE)
    p2.stdin.write(out.replace('<data>','<string>').replace('</data>','</string>'))
    out2, err2 = p2.communicate()
    return json.loads(out2)
    
def plist_to_dictionary(filename):
    "Pipe the binary plist through plutil and parse the JSON output"
    with open(filename, "rb") as f:
        content = f.read()
    
    args = ["plutil", "-convert", "json", "-o", "-", "--", "-"]
    p = Popen(args, stdin=PIPE, stdout=PIPE)
    p.stdin.write(content)
    out, err = p.communicate()
    return json.loads(out)


#aa=plist_to_dictionary('overrides_N56_N61.pri')
#print aa['Maverick']['PRI Revision']
