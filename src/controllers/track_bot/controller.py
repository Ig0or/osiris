from src.domain.validators.track_bot.validators import ChallengeInputValidator
from src.services.track_bot.service import TrackBotService


class TrackBotController:
    @staticmethod
    async def subscribe_web_hook(challenge_input: ChallengeInputValidator):
        challenge_result = await TrackBotService.subscribe_web_hook(challenge_input=challenge_input)

        return challenge_result