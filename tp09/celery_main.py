from celery import Celery

def main():
    app = Celery('celery_tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
    result = app.send_task("celery_tasks.add",args=[2,5])
    print(result.get() )

if __name__=='__main__':
    main()
