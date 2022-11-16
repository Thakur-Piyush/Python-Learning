from fastapi import FastAPI

app = FastAPI() 

@app.get("/")  #path decoration.Operation(Path)
def read_root(): #Function
    return {"Hello": {'Name':'Piyush'}}

@app.get('/about')
def about():
    return 'About page'

@app.get('/blog/{id}')
def show(id:int):
    return {'ID':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{'1','2'}}

