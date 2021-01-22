<rasaeco-meta>
{
    "title": "Fall Risk",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Manuel Menendez <manuel.menendez@vias.es>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "risk_management", "nature": "specific" }
    ],
    "volumetric": [
        {
            "aspect_from": "analytics", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        }    
    ]
}
</rasaeco-meta>

## Summary

This scenario specifies the details of <scenarioref name="risk_management" /> for 
<ref name="fall_risk" />s.

## Models

*Intentionally left empty.*

## Definitions

<def name="health_and_safety_manager">

Health and safety manager is a <ref name="risk_management#risk_manager" /> that takes care
of the fall risks on a construction site.

</def>

<def name="fall_risk">

Fall risk is a <ref name="risk_management#risk" /> where a person risks falling and getting hurt.

It is a <ref name="risk_management#risk_type" /> "fall risk". 

</def>

## Scenario

The <ref name="health_and_safety_manager" /> uses <scenarioref name="risk_management" /> to
define <ref name="fall_risk" />s.

*The preceding aspect sections intentionally left empty.*

### Analytics

The <ref name="health_and_safety_manager" /> should be able to get an overview of 
the <ref name="fall_risk" />s in a table.

A table is not free-form, but follows a widely used structured for capturing and organizing
<ref name="fall_risk" />s. 

*The remaining sections intentionally left empty.*
