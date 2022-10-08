from src.domain.validators.track_bot.validators import ChallengeInputValidator
from src.services.auth.service import AuthService


class TrackBotService:
    @staticmethod
    async def subscribe_web_hook(challenge_input: ChallengeInputValidator) -> int:
        is_token_valid = await AuthService.validate_access_token(token=challenge_input.hub_verify_token)

        if challenge_input.hub_mode == "subscribe" and is_token_valid:
            return challenge_input.hub_challenge
