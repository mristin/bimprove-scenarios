<rasaeco-meta>
{
    "title": "Risk Planning",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "risk_management", "nature": "in planning" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "as-planned",
            "phase_from": "planning", "phase_to": "planning",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "analytics", "aspect_to": "analytics",
            "phase_from": "planning", "phase_to": "planning",
            "level_from": "site", "level_to": "site"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario is a sub-scenario of <scenarioref name="risk_management" /> which considers
how the risks are planned and identified during the planning phase (and later updated
during the construction, but at a much slower pace).

## Scenario

### As-planned

**Specification of the <ref name="risk_management#risk" />s**.
There should be an application so that the <ref name="risk_management#risk_manager" /> can easily convert 
a <ref name="scheduling#task" /> to a <ref name="risk_management#risk" /> and capture the additional
information such as the <ref name="risk_management#risk_zone" />.

There should be also a <ref name="risk_management#risk" /> management application so that 
the <ref name="risk_management#risk_manager" /> can also create, list and modify the <ref name="risk_management#risk" />s 
(together with the <ref name="risk_management#risk_zone" />s, time span *etc.*).

Mind that a <ref name="risk_management#risk" /> needs not be necessarily associated with a 
<ref name="scheduling#task" />.

<phase name="planning">The <ref name="risk_management#risk_manager"/> inputs the initial set of 
<ref name="risk_management#risk"/>s already known during the planning.</phase>

### Analytics

The distribution of the <ref name="risk_management#risk" />s over their 
<ref name="risk_management#risk_level" />s should be displayed along with the number of risks
identified.

We also need to display the corresponding distribution of the <ref name="scheduling#task" />s and
their associated risks (if the <ref name="scheduling#task" />s are already available during the
planning phase).
