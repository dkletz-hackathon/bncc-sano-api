from core.router import Router
from src.route.user import user_router
from src.route.category import category_router
from src.route.routine import routine_router
from src.route.event import event_router
from src.route.activity import activity_router
from src.route.location import location_router
from src.route.schedule import schedule_router

group_router = Router()
group_router.group("/user", user_router)
group_router.group("/category", category_router)
group_router.group("/routine", routine_router)
group_router.group("/event", event_router)
group_router.group("/activity", activity_router)
group_router.group("/location", location_router)
group_router.group("/schedule", schedule_router)

__all__ = [group_router]
