import os
import routes
import uvicorn
import parameters as params

app = routes.app

if __name__ == "__main__":

    PORT = int(params.SELF_PORT)


    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
