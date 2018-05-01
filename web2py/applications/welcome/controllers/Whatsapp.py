from subprocess import call
import shlex

def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def sendmessage():
    number = request.vars
    f = open("C:/Users/Umair/Desktop/whatsapp-framework-master/modules/hi_module.py","a+")
    f.write("\n       mac.send_message_to ('" + number['message'] + "', '" + number['number']  + "@s.whatsapp.net')")
    f.close()
    call(["bash", "path/start.sh"])

    return dict()