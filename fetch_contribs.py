

projects = dict({'Logging': {'duration': 5, 'score': 10, 'maxDays': 5, 'roleRequirement': {'C++': 3}}, 'WebServer': {'duration': 7, 'score': 10, 'maxDays': 7, 'roleRequirement': {'HTML': 3, 'C++': 2}},'WebChat': {'duration': 10, 'score': 20, 'maxDays': 20, 'roleRequirement': {'Python': 3, 'HTML': 3}}})
skills = dict({'C++': {'Anna': 2}, 'HTML': {'Bob': 5}, 'CSS': {'Bob': 5}, 'Python': {'Maria': 3}})
Occupied = []
project_contribs = dict()
pending_projs = []
project_ready = []
for proj in projects.keys():
    req = projects[proj]['roleRequirement']
    print(req)
    all_reqs_check = True # default true   
    for skill_req in req.keys():
        print("skill - ", skill_req)
        # check in available skills
        if skills.get(skill_req) != None:
            available_contribs = skills.get(skill_req) # available contrib for required skill
            print("Available contribs - ")
            print(available_contribs)
            has_skill = False
            if available_contribs == None:
                pending_projs.append(proj)
                print("no available contributors!")
                all_reqs_check = False
                break
            for contrib in available_contribs.keys():
                if contrib in Occupied:
                    print("Contributor " + contrib + " is occupied")
                    continue
                skill_level = available_contribs[contrib]
                if skill_level >= req[skill_req]:
                    # has required skill for project -> break and check for next requirement
                    Occupied.append(contrib)
                    has_skill = True
                    break
            if has_skill == False:
                pending_projs.append(proj)
                print("Skill level requirement not met for skill - " + skill_req)
                all_reqs_check = False              
        else:
            print("Skill " + skill_req + "not available!")
            pending_projs.append(proj)
            all_reqs_check = False
        print("Occupied contribs - ")
        print(Occupied)
    if all_reqs_check == True:
        project_ready.append(proj)
    else:
        print("Project added to pending proj")




print("Pending Projects : ")
print(pending_projs)
print("Project Ready : ")
print(project_ready)
print(project_contribs)




    
