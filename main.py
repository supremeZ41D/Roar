import typer
import sqlite3

# Initial variables
connect = sqlite3.connect("KJ_Bible")
cursor = connect.cursor()
app = typer.Typer()

@app.command()
def welcome(name: str):
    print(f"Welcome {name}, to Roar! An open-source CLI Bible tool.")

@app.command()
def books(mode: str='column'):
    """Books are printed in both column and row form"""
    query = """SELECT name FROM sqlite_schema"""
    result = cursor.execute(query).fetchall()

    for cell in result:
        if mode=='row':
            print(cell[0], end=' ')
        elif mode=='column':
            print(cell[0])


if __name__ == "__main__":
    app()
