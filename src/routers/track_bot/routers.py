from fastapi import APIRouter, Query, Depends

from src.controllers.track_bot.controller import TrackBotController
from src.domain.validators.track_bot.validators import ChallengeInputValidator


class TrackBotRouters:
    __track_bot_routers = APIRouter()

    @staticmethod
    def get_routers():
        return TrackBotRouters.__track_bot_routers

    @staticmethod
    @__track_bot_routers.get("/track_bot")
    async def subscribe_web_hook(challenge_input: ChallengeInputValidator = Depends(ChallengeInputValidator)):
        response = await TrackBotController.subscribe_web_hook(challenge_input=challenge_input)

        return response
