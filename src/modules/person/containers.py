from dependency_injector import containers, providers

from .engines.engine import PersonEngine
from .repositories.db_repo import PersonDBRepo
from ...db.connection import get_session_maker


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.api'])

    session_maker = providers.Singleton(get_session_maker)

    db_repo = providers.Factory(
        PersonDBRepo,
        session=session_maker
    )
    engine = providers.Factory(
        PersonEngine,
        repo=db_repo
    )
