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
from datasheets_openapi_client.models.multienancy_support import MultienancySupport
from datasheets_openapi_client.models.multiuser_support import MultiuserSupport
from datasheets_openapi_client.models.protocol_item import ProtocolItem

class TechnicalRequirements(BaseModel):
    """
    TechnicalRequirements
    """
    disk_unit: StrictStr = Field(...)
    gpu_unit: StrictStr = Field(...)
    multienancy_support: MultienancySupport = Field(...)
    multiuser_support: MultiuserSupport = Field(...)
    ram_unit: StrictStr = Field(...)
    dashboard: Optional[StrictStr] = None
    os: Optional[conlist(StrictStr)] = None
    protocol: Optional[conlist(ProtocolItem)] = None
    requirement_cpu: Optional[StrictStr] = None
    requirement_disk: Optional[StrictStr] = None
    requirement_gpu: Optional[StrictStr] = None
    requirement_ram: Optional[StrictStr] = None
    __properties = ["disk_unit", "gpu_unit", "multienancy_support", "multiuser_support", "ram_unit", "dashboard", "os", "protocol", "requirement_cpu", "requirement_disk", "requirement_gpu", "requirement_ram"]

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
    def from_json(cls, json_str: str) -> TechnicalRequirements:
        """Create an instance of TechnicalRequirements from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of multienancy_support
        if self.multienancy_support:
            _dict['multienancy_support'] = self.multienancy_support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multiuser_support
        if self.multiuser_support:
            _dict['multiuser_support'] = self.multiuser_support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in protocol (list)
        _items = []
        if self.protocol:
            for _item in self.protocol:
                if _item:
                    _items.append(_item.to_dict())
            _dict['protocol'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TechnicalRequirements:
        """Create an instance of TechnicalRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TechnicalRequirements.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TechnicalRequirements) in the input: " + obj)

        _obj = TechnicalRequirements.parse_obj({
            "disk_unit": obj.get("disk_unit"),
            "gpu_unit": obj.get("gpu_unit"),
            "multienancy_support": MultienancySupport.from_dict(obj.get("multienancy_support")) if obj.get("multienancy_support") is not None else None,
            "multiuser_support": MultiuserSupport.from_dict(obj.get("multiuser_support")) if obj.get("multiuser_support") is not None else None,
            "ram_unit": obj.get("ram_unit"),
            "dashboard": obj.get("dashboard"),
            "os": obj.get("os"),
            "protocol": [ProtocolItem.from_dict(_item) for _item in obj.get("protocol")] if obj.get("protocol") is not None else None,
            "requirement_cpu": obj.get("requirement_cpu"),
            "requirement_disk": obj.get("requirement_disk"),
            "requirement_gpu": obj.get("requirement_gpu"),
            "requirement_ram": obj.get("requirement_ram")
        })
        return _obj


