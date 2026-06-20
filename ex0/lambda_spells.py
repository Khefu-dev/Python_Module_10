#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    powers = list(map(lambda m: m['power'], mages))

    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Shadow Cloak', 'power': 60, 'type': 'armor'},
        {'name': 'Lightning Ring', 'power': 78, 'type': 'accessory'},
        {'name': 'Frost Blade', 'power': 88, 'type': 'weapon'},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")
    if len(sorted_artifacts) < 2:
        print("Not enough artifacts to compare")
    else:
        first, second = sorted_artifacts[0], sorted_artifacts[1]
        print(f"{first['name']} ({first['power']} power) comes before "
              f"{second['name']} ({second['power']} power)")

    mages = [
        {'name': 'Alex', 'power': 75, 'element': 'fire'},
        {'name': 'Jordan', 'power': 40, 'element': 'water'},
        {'name': 'Riley', 'power': 90, 'element': 'air'},
        {'name': 'Sam', 'power': 55, 'element': 'earth'},
    ]

    print("\nTesting power filter...")
    min_power = 50
    filtered_mages = power_filter(mages, min_power)
    for mage in filtered_mages:
        print(f"{mage['name']} ({mage['power']} power) "
              f"meets the {min_power} power threshold")

    spells = ['fireball', 'heal', 'shield']

    print("\nTesting spell transformer...")
    print(' '.join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
