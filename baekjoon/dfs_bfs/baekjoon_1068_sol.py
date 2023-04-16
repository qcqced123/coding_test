def dfs(y):
    global re
    for i in g[y]: # 루트 노드 연결 정보 순회 시작
        if not vist[i] and i !=en: # 아직 방문 안했고 삭제 대상 노드가 아닌 경우
            vist[i]=True
            if g[i]==[]:
                re+=1
            dfs(i)
        elif i==en and len(g[y])==1:#삭제된 노드때문에 리프노드가 된 경우!
            re+=1


n = int(input()) # 개수 입력 받고
g = [[] for _ in range(n)] # 그래프 구조 만들고
s = list(map(int,input().split())) # 연결 정보 받고

for i in range(n):
    if s[i]!=-1:
        g[s[i]].append(i)
    else:
        t = i # 원래 그래프 자료 구조에 연결 정보 넣고, 루트 노드 정보 저장

en = int(input()) # 삭제할 노드 정보 받고
re = 0 # 이건 뭔지 모르겠고
g[en]=[] # 삭제할 노드의 그래프 정보 업데이트, 아예 비워버림
vist = [False]*(n+1) # 방분 정보
vist[t]=True # 루트 노드 부터 시작
dfs(t)
print(re)