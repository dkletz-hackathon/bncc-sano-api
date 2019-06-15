from src.exception import *
from core.util import *
from flask import request
from src.model import Location, Routine


def get_routines():
    location_id = request.args.get("t")
    query_option = None

    if location_id:
        location = Location.get_or_none(Location.id == location_id)
        if location is None:
            raise SanoException(404, NOT_FOUND, "Location not found")

        query_option = Routine.location == location

    routines = Routine.select(Routine).join(Location).where(query_option)

    return respond_data([routine.to_dict() for routine in routines])


def get_routine_by_id(routine_id):
    routine = Routine.get_or_none(Routine.id == routine_id)
    if routine is None:
        raise SanoException(404, NOT_FOUND, "Routine not found")

    return respond_data(routine.to_dict(True))
