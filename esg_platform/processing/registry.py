from processing.handlers.sap import SAPHandler
from processing.handlers.utility import UtilityHandler
from processing.handlers.travel import TravelHandler

HANDLERS = {
    "SAP": SAPHandler(),
    "UTILITY": UtilityHandler(),
    "TRAVEL": TravelHandler(),
}


def get_handler(source_type):
    return HANDLERS.get(source_type.upper())