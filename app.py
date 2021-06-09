from fastapi import FastAPI

from src.config import routes, containers


def create_app() -> FastAPI:
    container = containers.init_app()
    container.config.from_yaml('config.yml')
    container.wire(modules=routes.get_routes())

    db = container.db()
    db.create_database()

    app = FastAPI()
    routes.init_app(app)
    app.container = container
    return app


app = create_app()
