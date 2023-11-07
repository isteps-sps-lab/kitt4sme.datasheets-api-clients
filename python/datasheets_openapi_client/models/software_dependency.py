# coding: utf-8

"""
    Datasheets Backend

    This is Datasheet backend API documentation. This is intended only for development purposes

    The version of the OpenAPI document: 1.0.1
    Contact: kari.kolehmainen@vtt.fi
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class SoftwareDependency(BaseModel):
    """
    SoftwareDependency
    """
    dependency_level: StrictStr = Field(...)
    module_link: StrictStr = Field(...)
    module_text: Optional[StrictStr] = None
    module_version: Optional[StrictStr] = None
    module_id: Optional[StrictStr] = None
    __properties = ["dependency_level", "module_link", "module_text", "module_version", "module_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SoftwareDependency:
        """Create an instance of SoftwareDependency from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SoftwareDependency:
        """Create an instance of SoftwareDependency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SoftwareDependency.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in SoftwareDependency) in the input: " + obj)

        _obj = SoftwareDependency.parse_obj({
            "dependency_level": obj.get("dependency_level"),
            "module_link": obj.get("module_link"),
            "module_text": obj.get("module_text"),
            "module_version": obj.get("module_version"),
            "module_id": obj.get("module_id")
        })
        return _obj


