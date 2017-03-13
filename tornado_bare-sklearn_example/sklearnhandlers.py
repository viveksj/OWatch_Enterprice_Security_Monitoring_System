

#!/usr/bin/python

from pymongo import MongoClient
import tornado.web

from tornado.web import HTTPError
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
import pandas as pd
from basehandler import BaseHandler     
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import pickle
from bson.binary import Binary
import json
import numpy as np
import xlrd
import math

class PrintHandlers(BaseHandler):
    def get(self):
        '''Write out to screen the handlers used
        This is a nice debugging example!
        '''
        self.set_header("Content-Type", "application/json")
        self.write(self.application.handlers_string.replace('),','),\n'))


class SendUpdate(BaseHandler):
    def post(self):
        '''Regular updates about the Guard on reaching checkpoint
        # '''
        guard_id = self.get_argument("guard_id")
        print(guard_id)
        current_checkpoint = self.get_argument("current_checkpoint")
        print(current_checkpoint)
        next_checkpoint  = self.get_argument("next_checkpoint")
        print(next_checkpoint)
        data = {'Checkpoint No.': [current_checkpoint],
                'Guard No.': [guard_id],
                'Next Checkpoint': [next_checkpoint]} 
        if guard_id=="Guard1":
            writer = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/spreadsheet1.xls")

        if guard_id=="Guard2":
            writer = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/spreadsheet2.xls")

        table = pd.DataFrame(data)
        table.to_excel(writer)
        writer.save()

class PostFreq(BaseHandler):
    def post(self):
        '''Regular updates about the Covert Channel on iPhone device of Guard at reaching checkpoint 
        # '''
        frequency_received = math.trunc(float(self.get_argument("freq")))

        print(frequency_received)
        data1 = {'Frequency Received': [frequency_received]} 
        if (frequency_received < 19550):
            writer1 = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/channelA.xls")

        if (20000 < frequency_received):
            writer1 = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/channelB.xls")

        table1 = pd.DataFrame(data1)
        table1.to_excel(writer1)
        writer1.save()       

class GuardCurrentActivityUpdate(BaseHandler):
    def post(self):
        '''Activity of Guard - Running, Walking and Standing
        # '''
        guard_id = self.get_argument("guard_id")
        print(guard_id)        
        current_guard_activity  = self.get_argument("current_guard_activity")
        print(current_guard_activity)
        
        data = {'Activity': [current_guard_activity]} 
        if guard_id=="Guard1":
            writer = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardactivity1.xls")

        if guard_id=="Guard2":
            writer = pd.ExcelWriter("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardactivity2.xls")

        table = pd.DataFrame(data)
        table.to_excel(writer)
        writer.save()        

class DelayStatus(BaseHandler):
    def get(self):
    	'''Delay status - Alarm of Guard to Checkpoint
        # '''
        guard_id = self.get_argument("guard_id")
        print (guard_id)
        if guard_id=="Guard1":
            guardupdate = xlrd.open_workbook("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate1.xls")
        if guard_id=="Guard2":
            guardupdate = xlrd.open_workbook("/Users/CH484-mac1/Desktop/ML-ModuleB_Dec10_PostWorking/project/guardupdate2.xls")
        guardupdate = guardupdate.sheet_by_index(0)
        guardupdate = guardupdate.cell(1,1).value
        print(guardupdate)
        self.write_json({"stat":guardupdate})

