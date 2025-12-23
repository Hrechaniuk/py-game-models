import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as read_file:
        players = json.load(read_file)
    for name, info in players.items():
        race_obj, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]

        )
        if info["guild"] is None:
            guild_obj = None
        else:
            guild_obj, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        player_obj, _ = Player.objects.get_or_create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race_obj,
            guild=guild_obj
        )

        for skill in info["race"]["skills"]:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )


if __name__ == "__main__":
    main()
