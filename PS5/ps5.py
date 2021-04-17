# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:

        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)
        # print(description)
       

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            # pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)

    return ret



class NewsStory(object):
    def __init__ (self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate  

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
    

# PHRASE TRIGGERS

class PhraseTrigger (Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    def is_word_in(self,text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        word_list = text.split(' ')
        while '' in word_list:
            word_list.remove('')
        phrase1 =self.phrase
        if self.phrase[-1] != " ":
            phrase1+=" "
        story=""
        for wor in word_list:
            story+= wor +" "
        return phrase1 in story

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    def evaluate(self,text):
        booga = text.get_title()
        if self.is_word_in(booga) == True:
            return True
        

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    def evaluate(self, story):
        booga = story.get_description()
        if self.is_word_in(booga) == True:
            return True


# TIME TRIGGERS
class TimeTrigger(Trigger):
    def __init__(self,time):
        boo = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        self.DateTime = boo

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        poop = story.get_pubdate()       
        if poop < self.DateTime:
            return True

class AfterTrigger(TimeTrigger):
    def evaluate(self,story):
        poop1 = story.get_pubdate()
        if poop1> self.DateTime:
            return True
        
# COMPOSITE TRIGGERS

class NotTrigger(Trigger):
    def __init__ (self, timetrig):
        self.timetrig = timetrig
    def evaluate (self,story):
        return not self.timetrig.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__ (self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
    def evaluate(self,story):
        if (self.trig1.evaluate(story)==True) and (self.trig2.evaluate(story)==True):
            return True
class OrTrigger(Trigger):
    def __init__ (self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
    def evaluate(self,story):
        if (self.trig1.evaluate(story)==True) or (self.trig2.evaluate(story)==True):
            return True
        if (self.trig1.evaluate(story)==True) and (self.trig2.evaluate(story)==True):
            return True        
#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    pop =[]
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                pop.append(story)
    return pop



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    trig_dict = {}
    trig_list = []
    for i in range(len(lines)):
        trig = lines[i].split(',')

        if trig[1] == 'TITLE':
            trig_dict[trig[0]] = TitleTrigger(trig[2])
        elif trig[1] == 'DESCRIPTION':
            trig_dict[trig[0]] = DescriptionTrigger(trig[2])
        elif trig[1] == 'AFTER':
            trig_dict[trig[0]] = AfterTrigger(trig[2])
        elif trig[1] == 'BEFORE':
            trig_dict[trig[0]] = BeforeTrigger(trig[2])
        elif trig[1] == 'NOT':
            trig_dict[trig[0]] = NotTrigger(trig[2])
        elif trig[1] == 'AND':
            trig_dict[trig[0]] = AndTrigger(trig_dict[trig[2]], trig_dict[trig[3]])
        elif trig[0] == 'ADD':
            for x in range(1, len(trig)):
                trig_list.append(trig_dict[trig[x]])

    return trig_list



SLEEPTIME = 60 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("kumbh mela")
        # t2 = DescriptionTrigger("india")
        # t3 = DescriptionTrigger("corona")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # # # Problem 11
        # # # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Getting . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("https://news.google.com/news/rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("News Parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

