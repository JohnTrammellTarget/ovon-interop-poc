import sys
import Router.Logger as Logger
import KSR

def mod_init():
    KSR.info(">>>>> from Python mod_init()")
    return kamailio();


class kamailio:

    def __init__(self):
        KSR.info(">>>>> in kamailio.__init__")

    def child_init(self, rank):
        KSR.info(f">>>>> in kamailio.child_init({rank})")
        return 0

    def ksr_request_route(self, msg):
        """This is the equivalent of request_route{} in kamailio.cfg"""
        KSR.info(f">>>>> in kamailio.ksr_request_route({msg})")
        KSR.info(">>>>> method='%s' r-uri='%s'" % (KSR.pv.get("$rm"), KSR.pv.get("$ru")))


