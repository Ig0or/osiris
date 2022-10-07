from fastapi import APIRouter, Query, Depends

from src.controllers.track_bot.controller import TrackBotController
from src.domain.validators.track_bot.validators import ChallengeValidator


class TrackBotRouters:
    __track_bot_routers = APIRouter()

    @staticmethod
    def get_routers():
        return TrackBotRouters.__track_bot_routers

    @staticmethod
    @__track_bot_routers.get("/track_bot")
    async def validate_web_hook(challenge_input: ChallengeValidator = Depends()):
    # async def validate_web_hook(hub_mode: str = Query(alias="hub.mode"), hub_challenge: int = Query(alias="hub.challenge"), hub_verify_token=Query(alias="hub.verify_token")):
        # response = TrackBotController.validate_web_hook()
        return challenge_input.hub_challenge
        # return hub_challenge
