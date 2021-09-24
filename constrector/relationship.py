#Aggregation
class players:
    def __init__(self,name):
        self.name=name
class team:
    def __init__(self):
        self.players=[]
    def addplayers(self,player):
        self.players.append(player)
p=players("Sachin")
t=team()
t.addplayers(p)
print(t.players[0].name)
del t
print(p.name)