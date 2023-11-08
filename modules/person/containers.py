from dependency_injector import containers, providers

from ..db.connection import async_session
from .engines.engine import PersonEngine
from .repositories.db_repo import PersonDBRepo


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.api'])

    db_session = providers.Resource(async_session)

    db_repo = providers.Factory(
        PersonDBRepo,
        db_session=db_session
    )
    engine = providers.Factory(
        PersonEngine,
        repo=db_repo
    )
