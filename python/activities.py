import pandas as pd
path = "activities.jsonl"
df = pd.read_json(path_or_buf=path, lines=True, orient='records')

nodes = dict()
for i in range(len(df)):
    currNode = df["NODE_NAME"][i]
    grades = df["ACTIVITY_GRADE"][i].split(',')
    if currNode not in nodes:
        nodes[currNode] = set()
    for grade in grades:
        nodes[currNode].add(grade.strip())
# {'Node1': {'Kindergarten', 'PreK'}, 'Node2': {'1st Grade'}, 'Node3': {'Kindergarten', '1st Grade'}}
indices = {"Preschool": -2, "PreK": -1, "Kindergarten": 0,
           "1st Grade": 1, "2nd Grade": 2, "3rd Grade": 3,
           "4th Grade": 4, "5th Grade": 5}
minGrades = dict()
for node in nodes:
    currMin = ""
    currIndex = 10
    for grade in nodes[node]:
        if indices[grade] < currIndex:
            currIndex = indices[grade]
            currMin = grade
    minGrades[node] = currMin

df['MIN_NODE_GRADE'] = [None for i in range(len(df))]
for i in range(len(df)):
    currNode = df["NODE_NAME"][i]
    minGrade = minGrades[currNode]
    df['MIN_NODE_GRADE'][i] = minGrade

print(df)

