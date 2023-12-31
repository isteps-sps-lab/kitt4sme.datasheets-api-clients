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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from datasheets_openapi_client.models.benefits import Benefits
from datasheets_openapi_client.models.category import Category
from datasheets_openapi_client.models.features import Features
from datasheets_openapi_client.models.productiveaxis import Productiveaxis
from datasheets_openapi_client.models.usecase import Usecase

class Context(BaseModel):
    """
    Context
    """
    benefits: Benefits = Field(...)
    category: Category = Field(...)
    features: Features = Field(...)
    productiveaxis: Productiveaxis = Field(...)
    usecase: Usecase = Field(...)
    description: Optional[StrictStr] = None
    industry: Optional[conlist(StrictStr)] = None
    __properties = ["benefits", "category", "features", "productiveaxis", "usecase", "description", "industry"]

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
    def from_json(cls, json_str: str) -> Context:
        """Create an instance of Context from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of benefits
        if self.benefits:
            _dict['benefits'] = self.benefits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of productiveaxis
        if self.productiveaxis:
            _dict['productiveaxis'] = self.productiveaxis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usecase
        if self.usecase:
            _dict['usecase'] = self.usecase.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Context:
        """Create an instance of Context from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Context.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Context) in the input: " + obj)

        _obj = Context.parse_obj({
            "benefits": Benefits.from_dict(obj.get("benefits")) if obj.get("benefits") is not None else None,
            "category": Category.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "features": Features.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "productiveaxis": Productiveaxis.from_dict(obj.get("productiveaxis")) if obj.get("productiveaxis") is not None else None,
            "usecase": Usecase.from_dict(obj.get("usecase")) if obj.get("usecase") is not None else None,
            "description": obj.get("description"),
            "industry": obj.get("industry")
        })
        return _obj


