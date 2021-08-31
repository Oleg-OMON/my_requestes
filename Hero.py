import requests
hero_list = []

class Hero():
    def __init__(self, name):
        self.name = name
        self.response = requests.get("https://superheroapi.com/api/2619421814940190/search/" + self.name)
        self.result = self.response.json()['results']
        for element in self.result:
            for key, value in element.items():
                if key == 'id':
                    self.id = value
                if key == 'powerstats':
                    for stats , param in value.items():
                         if stats == 'combat':
                            self.combat = int(param)
                         elif stats == 'durability':
                            self.durability = int(param)
                         elif stats == 'intelligence':
                            self.intelligence = int(param)
                         elif stats == 'power':
                            self.power = int(param)
                         elif stats == 'speed':
                            self.speed = int(param)
                         elif stats == 'strength':
                            self.strength = int(param)
            break
        hero_list.append(self)

    def __str__(self):
        result = (f'name: {self.name}\n'
                  f'id: {self.id}\n'
                  f'durability: {self.durability}\n'
                  f'intelligence: {self.intelligence}\n'
                  f'power: {self.power}\n'
                  f'speed: {self.speed}\n'
                  f'strength: {self.strength}\n'
                  '\n')
        return result

def intelligence_hero():
    if len(hero_list) != 0:
        list_of_intelligence = []
        for element in hero_list:
            list_of_intelligence.append(element.intelligence)
        list_of_intelligence.sort()
        for element in hero_list:
            if element.intelligence == list_of_intelligence[-1]:
                print(f'{element.name} - самый умный из созданных персонажей!')
    else:
        print('Для сравнения интеллекта героев, их нужно создать=)')



hulk = Hero('Hulk')
cap_am = Hero('Captain America')
thanos = Hero('Thanos')
print(hulk, cap_am, thanos)


intelligence_hero()


