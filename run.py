from _init_ import app,db

app.env = "development"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=1010)    
