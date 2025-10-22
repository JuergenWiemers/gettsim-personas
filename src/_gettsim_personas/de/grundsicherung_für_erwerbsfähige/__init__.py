import datetime
from pathlib import Path

from _gettsim_personas.persona_objects import OrigPersonaOverTime

# Singles with 0-5 children
Single0Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_0_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Single1Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_1_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Single2Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_2_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Single3Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_3_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Single4Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_4_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Single5Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "single_5_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

# Couples with 0-5 children
Couple0Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_0_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Couple1Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_1_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Couple1Child = Couple1Children  # Backwards compatibility alias

Couple2Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_2_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Couple3Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_3_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Couple4Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_4_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)

Couple5Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_5_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)


Couple1ChildInKarenzzeit = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_1_child_in_karenzzeit.py",
    start_date=datetime.date(2023, 1, 1),
    error_if_not_implemented=(
        "Karenzzeit for Bürgergeld is not relevant before 2023. Use the "
        "'grundsicherung_für_erwerbsfähige.Couple1Child' persona instead."
    ),
)


Couple5Children = OrigPersonaOverTime(
    path_to_persona_elements=Path(__file__).parent / "couple_5_children.py",
    start_date=datetime.date(2005, 1, 1),
    error_if_not_implemented=(
        "These personas are available from 2005 because basic income support is not "
        "implemented in GETTSIM before 2005."
    ),
)


__all__ = [
    # Singles
    "Single0Children",
    "Single1Children",
    "Single2Children",
    "Single3Children",
    "Single4Children",
    "Single5Children",
    # Couples
    "Couple0Children",
    "Couple1Children",
    "Couple2Children",
    "Couple3Children",
    "Couple4Children",
    "Couple5Children",
    # Special cases
    "Couple1ChildInKarenzzeit",
    # Backwards compatibility
    "Couple1Child",
]
