import re

from .base import RegexDetector
from ..filth import VehicleFilth


class VehicleDetector(RegexDetector):
    """
    Use regex to find Vehicle Registration Plates (VRPs)
    """
    filth_cls = VehicleFilth
