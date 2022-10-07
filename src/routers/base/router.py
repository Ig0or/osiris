from fastapi import FastAPI

from src.routers.track_bot.routers import TrackBotRouters


class BaseRouter:
    app = FastAPI()

    @staticmethod
    def __register_track_bot_routers():
        track_bot_routers = TrackBotRouters.get_routers()
        BaseRouter.app.include_router(router=track_bot_routers)

        return BaseRouter.app

    @staticmethod
    def register_routers():
        BaseRouter.__register_track_bot_routers()

        return BaseRouter.app
