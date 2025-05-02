from apscheduler.schedulers.blocking import BlockingScheduler
import coin
from mylogger import  make_logger

logging = make_logger("coin.log","job_get_coin")
def job_get_coin():
    logging.info("코인 데이터 저장 시작")
    try:
        coin.get_coin()
    except Exception as e:
        logging.error(f"에러 발생!:{e}")
    logging.info("저장 완료!!")

sched = BlockingScheduler()
# 10분마다 수집
sched.add_job(job_get_coin, 'interval', minutes=10)
logging.info("coin_scheduler 시작")
sched.start()