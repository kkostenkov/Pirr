import os
import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

questList = []

def make_quest_list():
    #print(questList)
    questList = []
    for fileName in os.listdir("quests/"):
        if fileName[-4:] == ".txt":
            questList.append(fileName[:-4])
    #print(questList)
    return questList

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(make_quest_list()))
        #self.write("You requested list of available quests/n")

class QuestHandler(tornado.web.RequestHandler):
    def get(self, quest_id):
        #self.write("You requested the quest " + quest_id + "\n")
        print(quest_id)
        with open(str("quests/" + quest_id)+".txt", "r") as quest:
            self.write( quest.read())





def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/quest/(\w+)", QuestHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    
    main()
    
