import randdom
stress = 10
DailyConfirmedCases = 0
allConfirmedCases = 0
dailyDeath = 0
allDeath = 0
Reintroduce = 1.2
delta = randdom.randint(10, 20)
omicron = randdom.randint(10, 20)
withChorona = randdom.randint(30, 40)
weeks = 0
distancingStages = 0
print('코로나 거리두기 단계 시뮬레이터 게임입니다. 플레이어는 거리두기 단계를 지정할 수 있으며 스트레스 지수가 100 이상 혹은 일일확진자수가 5000명이상 혹은 전체 사망자수가 10000명이 넘으면 게임에서 패배합니다.')
while stress < 100 and DailyConfirmedCases < 5000 or allDeath <10000:
    entrance = randdom.randint(5, 30)
    print(weeks, '주차, 스트레스 지수:', stress, ', 일일 확진자 수:', DailyConfirmedCases, ', 치료중인 환자 수:', allConfirmedCases, ', 일일 사망자 수:', dailyDeath, ', 전체 사망자 수:', allDeath, ', 해외 입국자 수:', entrance)
    if weeks == 0:
        print('국내에서 코로나 19 확진자가 처음 검출 되었습니다. 첫 검출 확진자 수는 ',entrance,'로 모두 해외 입국자입니다.' )
    

