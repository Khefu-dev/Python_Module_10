#!/usr/bin/env python3
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    raise NotImplementedError


def power_validator(min_power: int) -> Callable:
    raise NotImplementedError


def retry_spell(max_attempts: int) -> Callable:
    raise NotImplementedError


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        raise NotImplementedError

    def cast_spell(self, spell_name: str, power: int) -> str:
        raise NotImplementedError


def main() -> None:
    print("Testing spell timer...")

    print("\nTesting retrying spell...")

    print("\nTesting MageGuild...")


if __name__ == "__main__":
    main()
