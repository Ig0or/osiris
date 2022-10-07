from dataclasses import dataclass

from pydantic import BaseModel, Field
from fastapi import Query


@dataclass
class ChallengeValidator():
    hub_mode: str = Query(None, alias="hub.mode")
    hub_challenge: int = Query(None, alias="hub.challenge")
    hub_verify_token: str = Query(None, alias="hub.verify_token")

    # class Config:
    #     allow_population_by_field_name = True