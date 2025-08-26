import os

import routes
import uvicorn

app = routes.app

if __name__ == "__main__":

    PORT = int(os.getenv("PORT", 8001))


    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
