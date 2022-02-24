fileName="b_better_start_small.in"
inputFile=open("D:/HashCode/input_data/"+fileName+".txt")
lines = inputFile.readlines()
filteredLines=[]
for line in lines:
	filteredLines.append(line.replace("\n",""))
	# print(line)
# print(filteredLines)
contributorCount, projectCount = map(int,lines[0].split())
# print(lines)
# print(contributorCount)
# print(projectCount)

contributorInputCount=0
contributors={}
parsingIndex=1
while(contributorInputCount<contributorCount):
	contributorInputCount=contributorInputCount+1
	inputLis=filteredLines[parsingIndex].split()
	parsingIndex=parsingIndex+1
	contributorName = inputLis[0]
	skillCount= int(inputLis[1])
	skillInputCount = 0
	skillMap={}
	while(skillInputCount<skillCount):
		skillInputCount=skillInputCount+1
		skillLis=filteredLines[parsingIndex].split()
		parsingIndex=parsingIndex+1
		skillName=skillLis[0]
		skillLevel=int(skillLis[1])
		skillMap[skillName]=skillLevel
	contributors[contributorName]=skillMap

projectMap={}
while(parsingIndex<len(filteredLines)):
	projectLis=filteredLines[parsingIndex].split()
	parsingIndex=parsingIndex+1
	projectName=projectLis[0]
	projectParams={}
	projectParams["duration"]=int(projectLis[1])
	projectParams["score"]=int(projectLis[2])
	projectParams["maxDays"]=int(projectLis[3])
	roleCount=int(projectLis[4])
	roleInputCount = 0
	roleMap={}
	while(roleInputCount<roleCount):
		roleInputCount=roleInputCount+1
		roleLis=filteredLines[parsingIndex].split()
		parsingIndex=parsingIndex+1
		roleName=roleLis[0]
		roleLevel=int(roleLis[1])
		roleMap[roleName]=roleLevel
	projectParams["roleRequirement"]=roleMap
	projectMap[projectName]=projectParams

print("contributors")
print(contributors)
# print("\nprojects")
# print(projectMap)

skillBasedContributorMap={}
for contributor in contributors:
	for skill in contributors[contributor]:		
		skillMap={}
		skillLevel=contributors[contributor][skill]
		skillMap[contributor]=skillLevel
		if(skill in skillBasedContributorMap):
			# skill.append(skillMap)
			# skillBasedContributorMap[skill].append(skillMap)
			skillBasedContributorMap[skill][contributor]=skillLevel
		else:
			skillBasedContributorMap[skill]=skillMap

print("\nskillBasedContributorMap")
print(skillBasedContributorMap)
