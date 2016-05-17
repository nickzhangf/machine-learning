import urllib2

# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# test URLError
# request = urllib2.Request("http://www.xxxxxxx.com");
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError, e:
#     print e.reason

# test HTTPError
request = urllib2.Request("http://www.csdn.net/cqcre")
try:
    urllib2.urlopen(request, timeout=1)
except urllib2.HTTPError, e:
    print e.code
    print e.reason