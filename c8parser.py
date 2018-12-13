#coding=utf-8
from html.parser import HTMLParser


class c8Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.gotflag=False
        self.firstc8name=""
        self.flag_name=False
        self.firstc8price=0
        self.flag_price=False

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and self.gotflag==False:
            if len(attrs) == 1 and attrs[0] == ('class',"items-box-name font-2"):
                self.flag_name=True
        if tag == 'div' and self.gotflag==False:
            if len(attrs) ==1 and attrs[0] == ('class',"items-box-price font-5"):
                self.flag_price= True

    def handle_data(self, data):
        if self.flag_name:
            self.firstc8name=data
            self.flag_name= False
        if self.flag_price:
            self.firstc8price=data
            self.flag_price= False
            self.gotflag = True
