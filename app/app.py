import os
import sys
import time
import os
import signal
import argparse
import logging

parentsDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(parentsDir)
print(parentsDir)

from smtm import *
import requests
import threading

class SmtmSimulator:
    def __init__(self, mode=None):
        self.logger = LogManager.get_logger("SmtmSimulator")
        self.__stop = False

        self.logger.info(mode)
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def main(self):
        operator = Operator()
        self.operator = operator
        dp = SimulatorDataProvider()
        operator.initialize(requests, threading, dp, None, None)
        operator.setup(2)
        if operator.start() is False:
            self.logger.warning("Fail start")
            return

        while not self.__stop:
            time.sleep(1)

    def stop(self, signum, frame):
        self.__stop = True
        if self.operator is not None:
            self.operator.stop()
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop Singing")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", help="operation mode", default=None)
    args = parser.parse_args()

    simulator = SmtmSimulator(args.mode)
    simulator.main()
