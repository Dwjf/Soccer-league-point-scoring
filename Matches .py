from Match_classes import Team,Match

England = Team("England")
Germany = Team("Germany")
m1 = Match(England,Germany,(2,1), False)
m2= Match(Germany, England,(5,7), True)
m3=Match(Germany, England,(2,3),False)
m4 = Match(Germany, England,(2,2), False)
list1 = [m1,m2,m3,m4]

for i in list1:
    i.pointCalc(i.teamA,i.teamB,i.result,i.penalty)

print(England.name,England.points,Germany.name,Germany.points)