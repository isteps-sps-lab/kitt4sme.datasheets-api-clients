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



from pydantic import BaseModel, Field
from datasheets_openapi_client.models.benefit2_fields import Benefit2Fields
from datasheets_openapi_client.models.benefit3_fields import Benefit3Fields

class Benefits(BaseModel):
    """
    Benefits
    """
    operator: Benefit3Fields = Field(...)
    production: Benefit2Fields = Field(...)
    quality: Benefit2Fields = Field(...)
    machine: Benefit2Fields = Field(...)
    __properties = ["operator", "production", "quality", "machine"]

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
    def from_json(cls, json_str: str) -> Benefits:
        """Create an instance of Benefits from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of operator
        if self.operator:
            _dict['operator'] = self.operator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of production
        if self.production:
            _dict['production'] = self.production.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of machine
        if self.machine:
            _dict['machine'] = self.machine.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Benefits:
        """Create an instance of Benefits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Benefits.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Benefits) in the input: " + obj)

        _obj = Benefits.parse_obj({
            "operator": Benefit3Fields.from_dict(obj.get("operator")) if obj.get("operator") is not None else None,
            "production": Benefit2Fields.from_dict(obj.get("production")) if obj.get("production") is not None else None,
            "quality": Benefit2Fields.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "machine": Benefit2Fields.from_dict(obj.get("machine")) if obj.get("machine") is not None else None
        })
        return _obj


