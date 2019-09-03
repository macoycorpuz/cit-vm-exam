def solution(totalMemory, foregroundApps, backgroundApps):
    output = []
    appIds, appMemories = [], []

    for fgApp in foregroundApps:
        for bgApp in backgroundApps:
            sumOfMemory = fgApp[1] + bgApp[1]
            appMemories.append(sumOfMemory)
            appIds.append([fgApp[0], bgApp[0]])

    

    return appIds, appMemories

print(solution(20, [[1,10],[2,15],[3,17]], [[1,3],[2,5]]))