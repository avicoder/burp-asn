from burp import IBurpExtender, IHttpListener
import socket
import urllib2
import json

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Check ASN")
        self._callbacks.registerHttpListener(self)
        print("ASN Finder extension loaded.")
        
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            httpService = messageInfo.getHttpService()
            host = httpService.getHost()
            
            try:
                ip_address = socket.gethostbyname(host)
                
                url = "https://ipinfo.io/{}/json".format(ip_address)
                response = urllib2.urlopen(url)
                data = json.load(response)
                org_name = data.get("org", "N/A").split(' ', 1)[-1]
                
                currentComment = messageInfo.getComment()
                newComment = "ASN: {}".format(org_name)
                if currentComment:
                    newComment = "{} | {}".format(currentComment, newComment)
                messageInfo.setComment(newComment)
            
            except Exception as e:
                print("Error processing IP {}: {}".format(host, e))
