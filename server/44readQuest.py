def read_quest(quest_id):
    print("You requested the quest " + str(quest_id))
    with open(str("quests/" + quest_id)+".txt", "r") as quest:
        return quest.read()

if __name__ == "__main__":
    number = input("Print quest number: ")
    print(read_quest(number))
    

