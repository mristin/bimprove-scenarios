<rasaeco-meta>
{
    "title": "Fire Risk",
    "contact": "Alberto Palomero <Alberto.Palomero@hrs.ch>, Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
        { "target": "risk_management", "nature": "specific" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "as-observed",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "scheduling", "aspect_to": "scheduling",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "safety", "aspect_to": "safety",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario specifies the details of <scenarioref name="risk_management" /> for 
<ref name="fire_risk" />s.

## Models

<model name="fire_risks">

This model captures all the <ref name="fire_risk" />s.

</model>

## Definitions

<def name="site_protection_manager">

Site protection manager is a <ref name="risk_management#risk_manager" /> that takes care
of various safety risks (including <ref name="fire_risk" />s) on a construction site.

</def>

<def name="fire_risk">

Fire risk is a <ref name="risk_management#risk" /> where there is a probability of fire breaking 
out.

It is a <ref name="risk_management#risk_type" /> "fire risk".

The fire risk is extended with the optional information about the <ref name="cool-down_period" />. 

</def>

<def name="hot_spot">

A hot spot is a spot on the construction site where there is a <ref name="fire_risk" /> at a given
time point.

</def>

<def name="cool-down_period">

This is a period indicating the period before the end of the work day that is necessary for the
equipment and material to cool down (and avoid fire).

</def>

## Scenario

The <ref name="site_protection_manager" /> uses <scenarioref name="risk_management" /> to
define <ref name="fire_risk" />s.

*The preceding aspect sections intentionally left empty.*

### As-planned

Certain <ref name="scheduling#task" />s require a <ref name="cool-down_period" /> (*e.g.*, 2 hours).
The <ref name="cool-down_period" /> can be either indicated by structured text in the body of a 
<ref name="scheduling#task" /> or added manually to <ref name="fire_risk" /> when the 
<ref name="scheduling#task" /> is converted to a <ref name="fire_risk" /> (see 
<scenarioref name="risk_management" />).

### As-observed

The <ref name="site_protection_manager" /> defines <ref name="hot_spot" />s as 
<ref name="uxv_recording#focus_spot" />s when there is a <ref name="fire_risk" />.

The <ref name="hot_spot" />s are inferred from the <ref name="scheduling#task" />s or based on
common practices (*e.g.*, inspect certain areas where heating might be stil on after the work
day).

*The aspect sections intentionally left empty.*

### Scheduling

The report is generated to show all the <ref name="scheduling#task" />s related to <ref name="fire_risk" />s for
which the <ref name="cool-down_period" /> is not respected.

### Safety

The <ref name="site_protection_manager" /> uses <scenarioref name="thermal_inspection" /> to
inspect the temperature of the <ref name="hot_spot" />s.

*The remaining sections intentionally left empty.*