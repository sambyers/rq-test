from redis import Redis
from rq import Queue
from rq.job import Job
from fastapi import FastAPI
from lib import long_task


app = FastAPI()

redis_conn=Redis(
    host='redis',
    port=6379,
)

@app.get("/task/{seconds}")
def task(seconds: int):
    q = Queue(connection=redis_conn)
    result = q.enqueue(long_task, seconds)
    return {'job_id': result.id}

@app.get("/job/{id}")
def get_job_id(id: str):
    job = Job.fetch(id, connection=redis_conn)
    return {'status': job.get_status()}
