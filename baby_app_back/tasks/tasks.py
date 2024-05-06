from celery import shared_task


@shared_task(bind=True)
#create any function  you want it to be allocated to celery
def test_func(self):
    #operation
    for i in range(10):
        print(i)
    return "done"