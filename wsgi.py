try:
    from src import app
except:
    from .src import app


if __name__ == '__main__':
    app.run()
