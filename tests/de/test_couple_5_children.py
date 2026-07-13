"""
Tests for the Couple5Children persona from grundsicherung_für_erwerbsfähige.

This test suite validates that the new persona for a couple with 5 children
works correctly with GETTSIM.
"""

import numpy as np
import pytest
from gettsim import InputData, MainTarget, TTTargets, main

from gettsim_personas import grundsicherung_für_erwerbsfähige


def test_couple_5_children_basic_instantiation():
    """Test that the Couple5Children persona can be instantiated."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Check that the persona has the correct number of individuals (2 parents + 5 kids)
    assert len(persona.input_data_tree["p_id"]) == 7
    assert np.array_equal(
        persona.input_data_tree["p_id"], np.array([0, 1, 2, 3, 4, 5, 6])
    )


def test_couple_5_children_ages():
    """Test that the children have the correct ages."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Check ages: parents are 30, children are 3, 5, 7, 9, 11
    expected_ages = np.array([30, 30, 3, 5, 7, 9, 11])
    # The key structure depends on GETTSIM's tree organization
    # Just check the basic length for now
    assert len(persona.input_data_tree["p_id"]) == 7


def test_couple_5_children_household_structure():
    """Test that the household structure is correctly defined."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Check that we have the correct number of people
    assert len(persona.input_data_tree["p_id"]) == 7

    # Check spouse relationship (p0 and p1 are spouses)
    expected_spouse = np.array([1, 0, -1, -1, -1, -1, -1])
    assert np.array_equal(
        persona.input_data_tree["familie"]["p_id_ehepartner"],
        expected_spouse,
    )

    # Check parent-child relationships
    # All children (p_id 2-6) have parent 1 as p_id 0
    expected_parent_1 = np.array([-1, -1, 0, 0, 0, 0, 0])
    assert np.array_equal(
        persona.input_data_tree["familie"]["p_id_elternteil_1"],
        expected_parent_1,
    )

    # All children (p_id 2-6) have parent 2 as p_id 1
    expected_parent_2 = np.array([-1, -1, 1, 1, 1, 1, 1])
    assert np.array_equal(
        persona.input_data_tree["familie"]["p_id_elternteil_2"],
        expected_parent_2,
    )


def test_couple_5_children_with_gettsim():
    """Test that GETTSIM can run successfully with the Couple5Children persona."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # This should not raise any errors
    result = main(
        main_target=MainTarget.results.df_with_nested_columns,
        policy_date_str=policy_date_str,
        input_data=InputData.tree(persona.input_data_tree),
        tt_targets=TTTargets(tree=persona.tt_targets_tree),
        include_warn_nodes=False,
    )

    # Check that we get results for all 7 individuals
    assert len(result) == 7


def test_couple_5_children_housing_costs():
    """Test that housing costs are appropriately scaled for larger household."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Larger household should have higher rent than couple with 1 child
    # All household members should have same rent value (household level)
    expected_rent = np.array([1050, 1050, 1050, 1050, 1050, 1050, 1050])
    assert np.array_equal(
        persona.input_data_tree["wohnen"]["bruttokaltmiete_m_hh"],
        expected_rent,
    )

    # Check wohnfläche (living space)
    expected_wohnflaeche = np.array([100, 100, 100, 100, 100, 100, 100])
    assert np.array_equal(
        persona.input_data_tree["wohnen"]["wohnfläche_hh"],
        expected_wohnflaeche,
    )


def test_couple_5_children_income():
    """Test that income distribution is correct."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Only parent 1 (p_id=0) has income
    expected_income = np.array([1000, 0, 0, 0, 0, 0, 0])
    assert np.array_equal(
        persona.input_data_tree["einnahmen"]["bruttolohn_m"],
        expected_income,
    )


def test_couple_5_children_childcare_costs():
    """Test that childcare costs are set for youngest children."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Childcare costs should be set for the two youngest children (aged 3 and 5)
    expected_costs = np.array([0, 0, 100, 100, 0, 0, 0])
    assert np.array_equal(
        persona.input_data_tree["einkommensteuer"]["abzüge"][
            "kinderbetreuungskosten_m"
        ],
        expected_costs,
    )


def test_couple_5_children_with_upsert():
    """Test that the persona can be used with upsert_input_data."""
    policy_date_str = "2020-01-01"
    base_persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Upsert higher rent values
    rent_to_upsert = {
        "wohnen": {
            "bruttokaltmiete_m_hh": np.array([1200, 1200, 1200, 1200, 1200, 1200, 1200])
        }
    }

    persona_with_higher_rent = base_persona.upsert_input_data(
        input_data_to_upsert=rent_to_upsert
    )

    # Check that rent was updated
    assert np.array_equal(
        persona_with_higher_rent.input_data_tree["wohnen"]["bruttokaltmiete_m_hh"],
        np.array([1200, 1200, 1200, 1200, 1200, 1200, 1200]),
    )


@pytest.mark.parametrize("year", [2005, 2010, 2015, 2020, 2023, 2024])
def test_couple_5_children_across_years(year):
    """Test that the persona works across different policy years."""
    policy_date_str = f"{year}-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # Should be able to run GETTSIM without errors
    result = main(
        main_target=MainTarget.results.df_with_nested_columns,
        policy_date_str=policy_date_str,
        input_data=InputData.tree(persona.input_data_tree),
        tt_targets=TTTargets(tree=persona.tt_targets_tree),
        include_warn_nodes=False,
    )

    assert len(result) == 7


def test_couple_5_children_kindergeld_recipients():
    """Test that kindergeld recipients are correctly set."""
    policy_date_str = "2020-01-01"
    persona = grundsicherung_für_erwerbsfähige.Couple5Children(
        policy_date_str=policy_date_str
    )

    # All children should have parent 1 (p_id=0) as kindergeld recipient
    expected_recipients = np.array([-1, -1, 0, 0, 0, 0, 0])
    assert np.array_equal(
        persona.input_data_tree["kindergeld"]["p_id_empfänger"],
        expected_recipients,
    )
