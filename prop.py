import websocket
import ssl
import time
import json
import pdb
from slacker import Slacker

import keys # fil to keep API key off github

slack = Slacker(keys.DAOkey)

DAOfunctions={
    "013cf08b": "proposals(uint256)",
    "0e708203": "rewardAccount()",
    "149acf9a": "daoCreator()",
    "237e9492": "executeProposal(uint256,bytes)",
    "2632bf20": "unblockMe()",
    "34145808": "totalRewardToken()",
    "4df6d6cc": "allowedRecipients(address)",
    "4e10c3ee": "transferWithoutReward(address,uint256)",
    "612e45a3": "newProposal(address,uint256,string,bytes,uint256,bool)",
    "643f7cdd": "DAOpaidOut(address)",
    "674ed066": "minQuorumDivisor()",
    "6837ff1e": "newContract(address)",
    "749f9889": "changeAllowedRecipients(address,bool)",
    "78524b2e": "halveMinQuorum()",
    "81f03fcb": "paidOut(address)",
    "82661dc4": "splitDAO(uint256,address)",
    "82bf6464": "DAOrewardAccount()",
    "8b15a605": "proposalDeposit()",
    "8d7af473": "numberOfProposals()",
    "96d7f3f5": "lastTimeMinQuorumMet()",
    "a1da2fb9": "retrieveDAOReward(bool)",
    "a3912ec8": "receiveEther()",
    "be7c29c1": "getNewDAOAddress(uint256)",
    "c9d27afe": "vote(uint256,bool)",
    "cc9ae3f6": "getMyReward()",
    "cdef91d0": "rewardToken(address)",
    "dbde1988": "transferFromWithoutReward(address,address,uint256)",
    "e33734fd": "changeProposalDeposit(uint256)",
    "e5962195": "blocked(address)",
    "e66f53b7": "curator()",
    "eceb2945": "checkProposalCode(uint256,address,uint256,bytes)"
}

def msg(text, channel):
    print text
    slack.chat.post_message(channel, text)

def listen():
    ws = websocket.create_connection("ws://socket.etherscan.io/wshandler",sslopt={"cert_reqs": False,"ssl_version": ssl.              PROTOCOL_SSLv3})
    ws.send("{\"event\": \"txlist\", \"address\": \"0xbb9bc244d798123fde783fcc1c72d3bb8c189413\"}")
    while True:
        result = json.loads(ws.recv_frame().data)
        if "result" in result.keys():
            for trans in result["result"]:
                if trans[u'input'][2:10] in DAOfunctions.keys():
                    msg("%s:%s Wei\n http://etherscan.io/tx/%s" %(DAOfunctions[trans[u'input'][2:10]],trans[u'value'],trans[u'hash']), "#bot")



        ws.send("{\"event\": \"ping\"}")
        time.sleep(20)

while True:
    try:
        listen()
    except:
        print "except"
        listen()

