import openpyxl as OPX
from openpyxl import load_workbook 
from openpyxl import Workbook 
import re
import requests
import sys
from tkinter import CENTER
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from time import sleep

class Variables():

    def __init__(self):
        self.EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"
        self.PHONE_REGEX = r"[\d]{2,4}-[\d]{2,4}-[\d]{2,4}"
        self.emailPattern = re.compile(self.EMAIL_REGEX)
        self.cfBool = True
        self.emailsListofLists = list()
        self.Categories = list()
        self.subCategories = list()
        self.tagsList = list()
        self.row_list = list()
        self.collective_list = list()
        self.PIncrement = int(0)
        self.filename = str()
        self.pureHtml = None
        self.textHtml = None
        self.parsedHtml = None
        self.pagesUrls = list()
        self.subpages = list()
        self.namesList = list()
        self.emailsList = list()
        self.phonesList = list()
        self.urlsList = list()
        #GetData Survey Here
        self.getNames = False
        self.getMailes = False
        self.getUrls = False
        self.getPhones = False
        self.getCNames = False
        self.currentSubpage = None
        self.emailCount = int(0)
        self.attributes = dict()
        self.attributesNames = dict()
        self.attributesEmails = dict()
        self.attributesUrls = dict()
        self.attributesPhones = dict()
        self.attributesCNames = dict()
        self.counter = 1
        self.tempList = []
        self.emailString = str()

class Variables_Gui():
    
    def __init__(self):
       pass


