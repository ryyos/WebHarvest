from time import perf_counter

from src.controller import DataAdmiralty
from src.controller import Shared
from src.controller import DataReviews
from src.controller import DataDivtic
from src.utils import Annotations
from src.utils import Stream
from src import Engine

def main() -> None:
    start: float = perf_counter()
    engine = Engine()

    engine.main.add_command(DataAdmiralty.task, name='admiralty')
    engine.main.add_command(Shared.task, name='shared')
    engine.main.add_command(DataReviews.task, name='reviews')
    engine.main.add_command(DataDivtic.task, name='divtic')

    engine.main()
    Stream.end(start, perf_counter())
    ...

if __name__ == '__main__':
    main()