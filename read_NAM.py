import iOS_Carrier_Bundle_Reader as iCBR
import os

bundles=os.listdir('.')

for bundle in bundles:
    if bundle.find('bundle')>0:
        files=os.listdir('./'+bundle+'/')
        for file in files:
            if file.find('.pri')>0:
                filename=bundle+'/'+file
                pri=iCBR.plist_to_dictionary(filename)
                if 'NAM - CDMA Settings' in pri:
                    if 'Preferred Mode' in pri['NAM - CDMA Settings']:
                        print bundle.replace('.bundle','')+'\t'+pri['NAM - CDMA Settings']['Preferred Mode']+'\t'+file.replace('.pri','')
#print iCBR.bplist_to_dictionary('carrier.plist')
#print iCBR.plist_to_dictionary('overrides_N56_N61.pri')