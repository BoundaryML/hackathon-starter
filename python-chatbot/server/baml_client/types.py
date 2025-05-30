###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum

from pydantic import BaseModel, ConfigDict

from typing_extensions import TypeAlias, Literal
from typing import Dict, Generic, List, Optional, TypeVar, Union


T = TypeVar('T')
CheckName = TypeVar('CheckName', bound=str)

class Check(BaseModel):
    name: str
    expression: str
    status: str
class Checked(BaseModel, Generic[T,CheckName]):
    value: T
    checks: Dict[CheckName, Check]

def get_checks(checks: Dict[CheckName, Check]) -> List[Check]:
    return list(checks.values())

def all_succeeded(checks: Dict[CheckName, Check]) -> bool:
    return all(check.status == "succeeded" for check in get_checks(checks))



class Role(str, Enum):
    
    User = "User"
    Assistant = "Assistant"
    Tool = "Tool"

class ComputeValue(BaseModel):
    type: Literal["compute_value"]
    arithmetic_expression: str

class GetWeatherReport(BaseModel):
    type: Literal["get_weather_report"]
    location: str

class Message(BaseModel):
    role: "Role"
    content: str
    timestamp: int

class MessageToUser(BaseModel):
    type: Literal["message_to_user"]
    message: str

class Query(BaseModel):
    message: str
    timestamp: int

class Resume(BaseModel):
    type: Literal["resume"]

class State(BaseModel):
    weather_report: Optional["WeatherReport"] = None
    recent_messages: List["Message"]

class WeatherReport(BaseModel):
    location: str
    temperature: int
    weather_status: str
    timestamp: int
