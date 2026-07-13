# Couple5Children Persona

## Overview

This new persona represents a married couple with **5 children aged 3, 5, 7, 9, and 11** who are eligible for basic subsistence benefits (Bürgergeld, formerly known as Arbeitslosengeld 2).

## Files Created

### 1. Persona Definition
- **File**: `src/_gettsim_personas/de/grundsicherung_für_erwerbsfähige/couple_5_children.py`
- **Description**: Defines the input data and targets for the persona

### 2. Registrations
- **File**: `src/_gettsim_personas/de/grundsicherung_für_erwerbsfähige/__init__.py`
  - Added `Couple5Children` to the module exports
- **File**: `src/gettsim_personas/grundsicherung_für_erwerbsfähige/__init__.py`
  - Added `Couple5Children` to the public API

### 3. Tests
- **File**: `tests/de/test_couple_5_children.py`
  - Comprehensive test suite with 15 test cases
  - All tests pass ✓

### 4. Demo Script
- **File**: `examples/demo_couple_5_children.py`
  - Demonstrates how to use the new persona

## Household Structure

- **Total members**: 7 (2 parents + 5 children)
- **Parent 1** (p_id=0): Age 30, primary earner with 1,000 EUR/month gross income
- **Parent 2** (p_id=1): Age 30, no income
- **Child 1** (p_id=2): Age 3
- **Child 2** (p_id=3): Age 5
- **Child 3** (p_id=4): Age 7
- **Child 4** (p_id=5): Age 9
- **Child 5** (p_id=6): Age 11

## Key Features

### Housing
- **Rent**: 900 EUR/month (bruttokaltmiete_m_hh)
- **Heating costs**: 80 EUR/month
- **Living space**: 100 m² (appropriate for larger family)
- **Rent level (Mietstufe)**: 5 (highest)

### Income
- Single earner household
- Parent 1 works 15 hours/week
- Gross monthly income: 1,000 EUR

### Childcare
- Childcare costs for the two youngest children (ages 3 and 5): 100 EUR/month each
- Costs are attributed to Parent 1

### Family Structure
- Parents are married (jointly taxed)
- All children have both parents registered
- Parent 1 receives Kindergeld for all children

## Available Date Range

- **Start date**: 2005-01-01
- **End date**: Present
- **Reason**: Basic income support (Bürgergeld/Arbeitslosengeld 2) is only implemented in GETTSIM from 2005 onwards

## Usage Example

```python
from gettsim import InputData, MainTarget, TTTargets, main
from gettsim_personas import grundsicherung_für_erwerbsfähige

# Create the persona
persona = grundsicherung_für_erwerbsfähige.Couple5Children(
    policy_date_str="2024-01-01"
)

# Run GETTSIM
result = main(
    main_target=MainTarget.results.df_with_nested_columns,
    policy_date_str=policy_date_str,
    input_data=InputData.tree(persona.input_data_tree),
    tt_targets=TTTargets(tree=persona.tt_targets_tree),
    include_warn_nodes=False,
)
```

## Varying Input Data

You can modify the persona's input data using the `upsert_input_data` method:

```python
import numpy as np

# Vary rent levels
rent_to_upsert = {
    "wohnen": {
        "bruttokaltmiete_m_hh": np.array([1200] * 7)  # All 7 members
    }
}

persona_with_higher_rent = persona.upsert_input_data(
    input_data_to_upsert=rent_to_upsert
)
```

## Test Coverage

The persona has been tested with:

1. **Basic instantiation** - Creating the persona
2. **Ages** - Correct ages for all family members
3. **Household structure** - Spouse and parent-child relationships
4. **GETTSIM integration** - Successfully runs with GETTSIM
5. **Housing costs** - Appropriate rent and living space
6. **Income distribution** - Correct income assignment
7. **Childcare costs** - Proper childcare cost allocation
8. **Upserting** - Ability to modify input data
9. **Multiple years** - Works across years 2005-2024
10. **Kindergeld recipients** - Correct assignment of benefits

All 15 dedicated tests pass, plus the persona is automatically included in the parametrized test suite that tests all personas across all years (62 total tests).

## Automatic Integration

The new persona is automatically discovered by the existing test infrastructure because it:
1. Is defined in the `grundsicherung_für_erwerbsfähige` module
2. Is an instance of `OrigPersonaOverTime`
3. Is exported in the module's `__all__` list

This means it will be tested alongside all other personas whenever the test suite runs.

## Comparison with Couple1Child

| Feature | Couple1Child | Couple5Children |
|---------|-------------|-----------------|
| Number of people | 3 | 7 |
| Number of children | 1 | 5 |
| Child ages | 6 | 3, 5, 7, 9, 11 |
| Rent | 600 EUR | 900 EUR |
| Living space | 65 m² | 100 m² |
| Heating costs | 50 EUR | 80 EUR |
| Childcare costs | 100 EUR (1 child) | 200 EUR (2 children) |
| Primary income | 1,000 EUR | 1,000 EUR |

## Notes

- Income from pensions, parental leave benefits, and subsistence benefits for the elderly are all set to zero
- This persona is specifically designed for computing mean-tested transfers for low-income households
- All pension-related input columns are overridden to avoid requiring complex pension data
- The persona assumes no receipt of Arbeitslosengeld (unemployment insurance benefits)
