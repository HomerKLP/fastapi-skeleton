from multiprocessing import cpu_count

bind = "0.0.0.0:8000"
worker_class = "uvicorn.workers.UvicornWorker"
workers = cpu_count() * 2 + 1
max_requests = 5000
max_requests_jitter = 512
capture_output = True
preload_app = True
