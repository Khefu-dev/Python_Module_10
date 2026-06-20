#!/usr/bin/env python3
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [s(target, power) for s in spells]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def shield(target: str, power: int) -> str:
    return f"Shields {target} with {power} defense"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def power_spell(target: str, power: int) -> str:
    return str(power)


def has_enough_power(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_spell = power_amplifier(power_spell, 3)
    original = power_spell("Dragon", 10)
    amplified = mega_spell("Dragon", 10)
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(has_enough_power, fireball)
    print(safe_fireball("Dragon", 10))
    print(safe_fireball("Dragon", 50))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield, lightning])
    for spell_result in sequence("Dragon", 50):
        print(spell_result)


if __name__ == "__main__":
    main()
