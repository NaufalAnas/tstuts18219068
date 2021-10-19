# Naufal Anas Nugrahanto (18219068)

import json
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

with open ('menu.json', 'r') as file_read :
    data = json.load (file_read)

app = FastAPI()

@app.get ('/')
def origin () :
    return {'Menu' : 'Item'}

@app.get ('/menu')
async def read_all () :
    return data

@app.get ('/menu/{item_id}')
async def read_menu (item_id : int) :

    for menu_item in data ['menu'] :
        if menu_item ['id'] == item_id :
            return menu_item

        raise HTTPException (
            status_code = 404,
            detail = f'Item not found'
        )

@app.post ('/menu')
async def add_menu (name : str) :   # Fungsi untuk Add Menu
    id = 1

    if (len(data["menu"]) > 0) :
        id = data ["menu"][len(data["menu"])-1]["id"]+1
    new_data = {'id' : id, 'name' : name}
    data ['menu'].append(dict(new_data))
    file_read.close()
    with open ("menu.json", "w") as write_file :
        json.dump (data, write_file, indent = 4)
    write_file.close ()

    return (new_data)

    raise HTTPEception (
        status_code=500,
        detail = f'Internal Server Error'
    )

@app.put ('/menu/{item_id}')
async def update_menu (item_id : int, name : str) :     # Fungsi untuk Update Menu

    for menu_item in data ['menu'] :
        if menu_item ['id'] == item_id :
            menu_item ['name'] = name
            file_read.close ()
            with open ("menu.json", "w") as write_file :
                json.dump (data, write_file, indent = 4)
            write_file.close ()

            return {"message" : "Data has been succesfully updated"}
        
        raise HTTPException (
            status_code = 404,
            detail = f'Item not found'
        )

@app.delete ('/menu/{item_id}')
async def delete_menu (item_id : int) :     # Fungsi untuk Delete Menu

    for menu_item in data ['menu'] :
        if menu_item ['id'] == item_id :
            data ['menu'].remove(menu_item)
            file_read.close()
            with open ("menu.json", "w") as write_file :
                json.dump (data, write_file, indent = 4)
            write_file.close()

            return {"message" : "Data has been succesfully deleted"}
        
        raise HTTPException (
            status_code = 404,
            detail = f'Item not found'
        )