import requests
from apscheduler.schedulers.blocking import BlockingScheduler

def kakao_news():
    url="http: // 3.36.128.81:3000/search_kakao/news"
    res=requests(url)

def exec_cron():
    print('exec cron')
sched = BlockingScheduler()

sched.add_job(kakao_news, 'interval', seconds=10)

# 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
# ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
sched.add_job(exec_cron, 'cron', minute='*/5', second='10, 30')

# 스케줄링 시작
sched.start()

