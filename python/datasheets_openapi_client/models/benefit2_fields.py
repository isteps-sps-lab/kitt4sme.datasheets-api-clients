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



from pydantic import BaseModel, Field, StrictBool

class Benefit2Fields(BaseModel):
    """
    Benefit2Fields
    """
    var_1: StrictBool = Field(..., alias="1")
    var_2: StrictBool = Field(..., alias="2")
    __properties = ["1", "2"]

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
    def from_json(cls, json_str: str) -> Benefit2Fields:
        """Create an instance of Benefit2Fields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Benefit2Fields:
        """Create an instance of Benefit2Fields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Benefit2Fields.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Benefit2Fields) in the input: " + obj)

        _obj = Benefit2Fields.parse_obj({
            "var_1": obj.get("1"),
            "var_2": obj.get("2")
        })
        return _obj


