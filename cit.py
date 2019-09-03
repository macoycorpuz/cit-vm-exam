def solution(totalMemory, foregroundApps, backgroundApps):
    output = []
    apps, appMemories = [], []
    tempMax = 0

    for fgApp in foregroundApps:
        for bgApp in backgroundApps:
            sumOfMemory = fgApp[1] + bgApp[1]
            appMemories.append(sumOfMemory)
            apps.append([fgApp[0], bgApp[0]])
            
    if not apps:
        return []
    
    if min(appMemories) > totalMemory:
        return []

    for memory in appMemories:
        if memory > tempMax and memory <= totalMemory:
            tempMax = memory

    for app, memory in zip(tuple(apps), tuple(appMemories)):
        if memory == tempMax:
            output.append(app)

    return output

print(solution(20, [[1,10],[2,15],[3,17]], [[1,3],[2,5]]))