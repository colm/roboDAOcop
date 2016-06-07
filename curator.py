import websocket
import ssl
import time
import json
import pdb
from slacker import Slacker

import keys

curators = {"1db3439a222c519ab44bb1144fc28167b4fa6ee6":"Vitalik Buterin",
    "b2c1b92f4bed7a173547cc601fb73a1254d10d26":"Aeron Buchanan",
    "0029218e1dab069656bfb8a75947825e7989b987":"Christian Reitwie_ner", #sorry Christian I cannot use the correct letter
    "cee96fd34ec793b05ee5b232b0110eac0cc3327e":"Taylor Gerring",
    "b274363d5971b60b6aca27d6f030355e9aa2cf23":"Viktor Tron",
    "c947faed052820f1ad6f4dda435e684a2cd06bb4":"Fabian Vogelsteller",
    "ae90d602778ed98478888fa2756339dd013e34c1":"Martin Becze",
    "e578fb92640393b95b53197914bd560b7bc2aac8":"Gustav Simonsson",
    "127ac03acfad15f7a49dd037e52d5507260e1425":"Vlad Zamfir",
    "0037a6b811ffeb6e072da21179d11b1406371c63":"Gavin Wood",
    "d1220a0cf47c7b9be7a2e6ba89f429762e7b9adb":"Alex Van de Sande"
}

slack = Slacker(keys.DAOkey)

print("starting")
def msg(text, channel, team):
    print text
    thedao.chat.post_message(channel, text)

def listen():
    ws = websocket.create_connection("ws://socket.etherscan.io/wshandler",sslopt={"cert_reqs": False,"ssl_version": ssl.              PROTOCOL_SSLv3})
    ws.send("{\"event\": \"txlist\", \"address\": \"0xda4a4626d3e16e094de3225a751aab7128e96526\"}")
    while True:
        result = json.loads(ws.recv_frame().data)
        if "result" in result.keys():
            for trans in result["result"]:
                if trans[u'from'] in curators.keys():
                    msg("%s: http://etherscan.io/tx/%s" %(curators[trans[u'from']], trans[u'hash']), "#dao_observation")
                else:
                    msg("%s: http://etherscan.io/tx/%s" %(trans[u'from'], trans[u'hash']), "#dao_observation")
                    #        print "Received '%s'" % result
        ws.send("{\"event\": \"ping\"}")
        time.sleep(20)

while True:
    try:
        listen()
    except:
        listen()

