from __future__ import annotations  # noqa: D104


class RunnerError(Exception):  # noqa: D101
    def __init__(self, message, exitcodes=None):  # noqa: D107
        super().__init__(message)
        self.exitcodes = {} if exitcodes is None else exitcodes


class Runner:  # noqa: D101
    def run(self):  # noqa: D102
        pass
