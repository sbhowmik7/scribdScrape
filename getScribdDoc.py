__author__ = 'sbhowmik'
'''-----------------------------------------------------------------------
This gets all the jpgs that constitutes the whole document. One needs to
 download the source for the document by right clicking and saving source as a html
 --------------------------------------------------------------------------'''
# Download Utility for files

def mydownload(url, fileName=None):
    import urllib2
    import shutil

    try:
        r = urllib2.urlopen(urllib2.Request(url))
    except:
        print 'Could not download ' + url
        return
    try: #Copy file
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)
    except:
        print 'Could not copy downloaded file ' + fileName
    finally:
        r.close()


import os.path
htmlSource = r'D:\Personal\test\Written\Python\Scribd_scrape\dwld_dir\Carson-W-Taylor-Power-System-Voltage-Stability-1994.htm'
foundId = False

with open(htmlSource,'r') as fd: # read the saved html file
    pgcount = 1
    for line in fd.xreadlines():
        if not foundId and 'assetprefix' in line.lower() : # Search for asserprefix which contains the ID
          id = line.split('=')[1].strip().strip(';').strip(r'"')
          foundId = True
        elif foundId : # search for lines with ID and images/pages on the line
            if id in line :
                if 'images' in line:
                    jpgName = line.split(r'images/')[1].split('.jpg')[0].strip('"')
                else:
                    jpgName = line.split(r'pages/')[1].split('.jsonp')[0].strip('"')

                url = 'http://htmlimg1.scribdassets.com/' + id +'/images/'+jpgName+'.jpg'
                opImg = str(pgcount).zfill(3)+'.jpg'
                if not os.path.isfile(opImg):
                    mydownload(url,opImg) #str(pgcount)+'.jpg'
                else:
                    print 'exists skipping ' +opImg
                pgcount = pgcount +1

if not foundId:
    print "WARNING!! Could not find ID. nothing done"
