import typer
import sqlite3
import pandas as pd

# Initial variables
connect_kj = sqlite3.connect("KJ_Bible")
cursor_kj = connect_kj.cursor()
connect_auth = sqlite3.connect('Authors_KJB.db')
cursor_auth = connect_auth.cursor()
app = typer.Typer()

@app.command()
def welcome(name: str):
    print(f"Welcome {name}, to Roar! An open-source CLI Bible tool.")

@app.command()
def books(mode: str='column', author: bool=False):
    """Books are printed in both column and row form"""

    def authors(place_list):
        df = pd.DataFrame(place_list, columns=['Book','Author'])
        print(df.groupby(['Author'])['Book'].value_counts().to_frame().rename(columns={'Book':'count'}).reset_index(level='Book')['Book'])

    query_kj = """SELECT name FROM sqlite_schema"""
    result_kj = cursor_kj.execute(query_kj).fetchall()
    query_auth = """SELECT Book,Author FROM Book2Author"""
    result_auth = cursor_auth.execute(query_auth).fetchall()

    place_list = []

    if mode=='row':
        for cell in result_kj:
            print(cell[0], end=' ')
    elif mode=='column' and author is False:
        for cell in result_kj:
            print(cell[0])
    elif mode=='column' and author is True:
        for cell in result_auth:
            #place_list.append(cell)
            print(cell[0] + ': ' + cell[1])

        #authors(place_list)



if __name__ == "__main__":
    app()
