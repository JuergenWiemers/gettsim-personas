"""
Example usage of the Couple5Children persona.

This script demonstrates how to use the new Couple5Children persona from the
grundsicherung_für_erwerbsfähige module to compute taxes and transfers for a
couple with 5 children aged 3, 5, 7, 9, and 11.
"""

from gettsim import InputData, MainTarget, TTTargets, main
from gettsim_personas import grundsicherung_für_erwerbsfähige

# Create a persona for a couple with 5 children
policy_date_str = "2024-01-01"
persona = grundsicherung_für_erwerbsfähige.Couple5Children(
    policy_date_str=policy_date_str
)

print("=" * 80)
print("Couple with 5 Children - Basic Subsistence Benefits Persona")
print("=" * 80)
print(f"\nPolicy Date: {policy_date_str}")
print(f"Number of individuals: {len(persona.input_data_tree['p_id'])}")
print(f"\nDescription:\n{persona.description}")

# Run GETTSIM to compute taxes and transfers
# Add specific Kinderzuschlag targets for debugging
additional_targets_tree = {
    "kinderzuschlag": {
        "betrag_m_bg": None,
        "erwachsenenbedarf_m_bg": None,
        "nettoeinkommen_eltern_m_bg": None,
    },
}

result = main(
    main_target=MainTarget.results.df_with_nested_columns,
    policy_date_str=policy_date_str,
    input_data=InputData.tree(persona.input_data_tree),
    tt_targets=TTTargets(tree=additional_targets_tree),
    include_warn_nodes=False,
)

print("\n" + "=" * 80)
print("Kinderzuschlag Debugging Information")
print("=" * 80)

# Display the Kinderzuschlag-specific targets
try:
    kiz_betrag = result.get(("kinderzuschlag", "betrag_m_bg"))
    kiz_erwachsenenbedarf = result.get(
        ("kinderzuschlag", "erwachsenenbedarf_m_bg")
    )
    kiz_nettoeinkommen = result.get(
        ("kinderzuschlag", "nettoeinkommen_eltern_m_bg")
    )
    
    if kiz_betrag is not None:
        print(f"\nkinderzuschlag__betrag_m_bg: {kiz_betrag[0]:.2f} EUR")
    if kiz_erwachsenenbedarf is not None:
        print(
            f"kinderzuschlag__erwachsenenbedarf_m_bg: "
            f"{kiz_erwachsenenbedarf[0]:.2f} EUR"
        )
    if kiz_nettoeinkommen is not None:
        print(
            f"kinderzuschlag__nettoeinkommen_eltern_m_bg: "
            f"{kiz_nettoeinkommen[0]:.2f} EUR"
        )
    
    # Show how much income is above the need threshold
    if kiz_nettoeinkommen is not None and kiz_erwachsenenbedarf is not None:
        diff = kiz_nettoeinkommen[0] - kiz_erwachsenenbedarf[0]
        print(f"\nIncome above need threshold: {diff:.2f} EUR")
        print(
            "This excess income reduces Kinderzuschlag at the "
            "entzugsrate_elterneinkommen rate"
        )
except Exception as e:
    print(f"Could not extract Kinderzuschlag debugging info: {e}")

print("\n" + "=" * 80)
print("Sample Results (first 7 rows)")
print("=" * 80)
print(result)

# Show some specific columns of interest
print("\n" + "=" * 80)
print("Key Transfer Columns")
print("=" * 80)

# Extract some key columns if they exist
try:
    buergergeld_col = None
    kindergeld_col = None
    
    for col in result.columns:
        if 'bürgergeld' in str(col).lower() and 'betrag' in str(col).lower():
            buergergeld_col = col
        if 'kindergeld' in str(col).lower() and 'betrag' in str(col).lower():
            kindergeld_col = col
    
    if buergergeld_col:
        print(f"\n{buergergeld_col}:")
        print(result[buergergeld_col])
    
    if kindergeld_col:
        print(f"\n{kindergeld_col}:")
        print(result[kindergeld_col])
        
except Exception as e:
    print(f"Could not extract specific columns: {e}")

print("\n" + "=" * 80)
print("Example: Varying Rent Levels")
print("=" * 80)

# Demonstrate upserting to vary rent levels
import numpy as np

rent_levels = [600, 800, 1000, 1200]
print(f"\nTesting different rent levels: {rent_levels}")

for rent in rent_levels:
    rent_to_upsert = {
        "wohnen": {
            "bruttokaltmiete_m_hh": np.array([rent] * 7)  # 7 household members
        }
    }
    
    persona_with_varied_rent = persona.upsert_input_data(
        input_data_to_upsert=rent_to_upsert
    )
    
    result_varied = main(
        main_target=MainTarget.results.df_with_nested_columns,
        policy_date_str=policy_date_str,
        input_data=InputData.tree(persona_with_varied_rent.input_data_tree),
        tt_targets=TTTargets(tree=persona_with_varied_rent.tt_targets_tree),
        include_warn_nodes=False,
    )
    
    print(f"\nRent = {rent} EUR/month:")
    print(f"  Number of rows in result: {len(result_varied)}")

print("\n" + "=" * 80)
print("Demo Complete!")
print("=" * 80)
