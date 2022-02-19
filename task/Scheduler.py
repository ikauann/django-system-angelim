from apscheduler.schedulers.background import BackgroundScheduler

from task import BlingGetProdutos

def start_scheduler():

    scheduler = BackgroundScheduler(timezone="America/Sao_Paulo")
    scheduler.add_job(BlingGetProdutos.exec, 'interval', seconds=1.5)
    scheduler.start()