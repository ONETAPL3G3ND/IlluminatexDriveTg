from fastapi import FastAPI, HTTPException, UploadFile, File, Response
from fastapi.responses import FileResponse
from FileManager import FileManager
from fastapi.staticfiles import StaticFiles
from DataOfServer import DataServer

app = FastAPI()
file_manager = FileManager()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def get_index_html():
    return FileResponse("static/index.html")


@app.get("/files/")
def get_all_files(response: Response):
    try:
        files = file_manager.GetAllObject()
        filelist = []
        for file in files:
            filelist.append({"name": file.FileName, "size": file.FileSize, "creation_date": file.FileData})
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
        return {"files": filelist}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/dataofmemory")
def data_of_server(response: Response):
    return DataServer().GetData()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
