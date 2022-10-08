from dataclasses import dataclass

from fastapi import Query


@dataclass
class ChallengeInputValidator:
    hub_mode: str = Query(alias="hub.mode")
    hub_challenge: int = Query(alias="hub.challenge")
    hub_verify_token: str = Query(alias="hub.verify_token")

