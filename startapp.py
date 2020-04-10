import logging
import time
from flask import g, request
from covid19estimator import create_app

app = create_app()
 
@app.before_request
def set_timer():
    g.start = time.time()

@app.after_request
def log(response):
    diff = int((time.time() - g.start) * 1000)
    log = f"{request.method} {request.path} {response.status_code} {diff} ms"
    app.logger.info(log)
    return response

if __name__ == "__main__":
    app.run()
