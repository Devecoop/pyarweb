from collections import defaultdict
from dataclasses import dataclass
from functools import wraps
from typing import Literal

from .models import OfferState

ACTIONS_PUBLISHER = defaultdict(dict)
ACTIONS_ADMIN = defaultdict(dict)

PROFILE_PUBLISHER = "publisher"
PROFILE_ADMIN = "admin"

CODE_CREATE = "create"
CODE_EDIT = "edit"
CODE_HISTORY = "history"
CODE_REJECT = "reject"
# CODE_COMMENT = "comment"
CODE_REACTIVATE = "reactivate"
CODE_DEACTIVATE = "deactivate"
CODE_REQUEST_MODERATION = "reqmod"
CODE_APPROVE = "approve"

ACTION = Literal[
    CODE_CREATE, CODE_EDIT, CODE_HISTORY, CODE_REJECT, CODE_REACTIVATE,
    CODE_DEACTIVATE, CODE_REQUEST_MODERATION, CODE_APPROVE
]


def register_action(func, profile):
    for state in func.valid_prev_states:
        if profile == PROFILE_PUBLISHER:
            ACTIONS_PUBLISHER[state][func.code] = func
        else:
            ACTIONS_ADMIN[state][func.code] = func


def check_state(func):
    @wraps(func)
    def wrapped(job_offer):
        if job_offer.state not in func.valid_prev_states:
            raise ValueError("Inconsistent state")
        else:
            result = func(job_offer)
            return result

    return wrapped


@dataclass
class Action:
    verbose_name: str
    code: str
    valid_prev_states: tuple


edit = Action(
    verbose_name="Editar",
    code=CODE_EDIT,
    valid_prev_states=(
        OfferState.ACTIVE, OfferState.DEACTIVATED, OfferState.REJECTED, OfferState.EXPIRED
    ),
)


reject = Action(
    verbose_name="Rechazar",
    code=CODE_REJECT,
    valid_prev_states=(OfferState.ACTIVE, OfferState.MODERATION,),
)


# comment = Action(
#     verbose_name="Comentar",
#     code=CODE_COMMENT,
#     valid_prev_states=(OfferState.MODERATION,),
# )


reactivate = Action(
    verbose_name="Reactivar",
    code=CODE_REACTIVATE,
    valid_prev_states=(OfferState.EXPIRED,),
)


deactivate = Action(
    verbose_name="Desactivar",
    code=CODE_DEACTIVATE,
    valid_prev_states=(OfferState.EXPIRED, OfferState.ACTIVE),
)


request_moderation = Action(
    verbose_name="Enviar a moderación",
    code=CODE_REQUEST_MODERATION,
    valid_prev_states=(OfferState.DEACTIVATED,),
)

approve = Action(
    verbose_name="Aprobar",
    code=CODE_APPROVE,
    valid_prev_states=(OfferState.MODERATION,),
)


get_history = Action(
    verbose_name="Historial",
    code=CODE_HISTORY,
    valid_prev_states=(
        OfferState.DEACTIVATED,
        OfferState.ACTIVE,
        OfferState.EXPIRED,
        OfferState.REJECTED
    ),
)

register_action(edit, PROFILE_PUBLISHER)
register_action(deactivate, PROFILE_PUBLISHER)
register_action(reactivate, PROFILE_PUBLISHER)
register_action(request_moderation, PROFILE_PUBLISHER)
register_action(get_history, PROFILE_PUBLISHER)

register_action(reject, PROFILE_ADMIN)
register_action(approve, PROFILE_ADMIN)
# register_action(comment, PROFILE_ADMIN)


ACTIONS = {
    PROFILE_PUBLISHER: dict(ACTIONS_PUBLISHER),
    PROFILE_ADMIN: dict(ACTIONS_ADMIN),
}


def _get_user_profile(user):
    """Get profile from user."""
    return PROFILE_ADMIN


def _is_owner(job_offer, user):
    """Check ownership of a job offfer."""
    return True


def validate_action(action_code: ACTION, user, job_offer=None):
    return True


def get_valid_actions(job_offer, user):
    """Return valid action for user."""
    state = job_offer.state
    # TODO: Implement profile states, now returning all only for testing.
    return ACTIONS_ADMIN[state] | ACTIONS_PUBLISHER[state]
    # profile = _get_user_profile(user)
    # state = job_offer.state

    # if profile == PROFILE_ADMIN:
    #     return ACTIONS_ADMIN[state]
    # else:
    #     if _is_owner(job_offer, user):
    #         return ACTIONS_PUBLISHER[state]
    #     else:
    #         raise ValueError()