class Team:
  def __init__(self, nev, project, role):
    self.nev = nev
    self.project = project
    self.role = role
    print("-- Developer létrehozva. --")
    print(nev + " a " + project + "-en dolgozik " + role + " szerepkörben.")
    developerek.append(self)

developerek = []
print()

alreadyCheckedProjects = []

vanEgyezes = False

while vanEgyezes == False:
    alreadyCheckedProjects.clear()
    print("Kérem adja meg a developer nevét, cégét, munkakörét: ")
    nev = input("nev: ")
    projekt = input("projekt: ")
    role = input("munkakör: ")
    developer = Team(nev, projekt, role)

    if len(developerek) > 1:
        for i in range(len(developerek)):
            same = []
            same.append(developerek[i])
           
            if developerek[i].project not in alreadyCheckedProjects:
                alreadyCheckedProjects.append(developerek[i].project)
          
            else:
                continue
            for j in range(len(developerek)):
                if j != i:
                   
                    if developerek[j].project == developerek[i].project:
                        same.append(developerek[j])
           
            if len(same) > 1:
                vanEgyezes = True
                for k in range(len(same)):
                    
                    if k != len(same) - 1:
                        print(same[k].nev + " és ", end="")
                  
                    else:
                        print(same[k].nev, end = "")
                print(" dolgoznak egy projekten.")
    print()
