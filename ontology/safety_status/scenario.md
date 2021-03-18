<rasaeco-meta>
{
    "title": "Safety Status",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
    ],
    "volumetric": [
        {
            "aspect_from": "safety", "aspect_to": "safety",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "device/person", "level_to": "device/person"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario covers the display of the <ref name="risk_status" /> based on various 
<ref name="risk_management#risk" />s (such as fall risks, fire risks *etc.*). 

## Models

*Intentionally left empty.*

## Definitions

<def name="alertee">

A person who needs to be alerted on his/her current risk level through the 
<ref name="smart_device" />.

Modeled as an <ref name="actor_management#actor" />.

</def>

<def name="smart_device">

<level name="device">A device such as a smart watch or a smartphone informing the 
<ref name="alertee" /> about the risk status.</level>

</def>

<def name="risk_status">

The risk status represents the various <ref name="risk_management#risk" />s in conjunction with
the location of the <ref name="alertee" />.

</def>

## Scenario

This is an experimental scenario.

The ideas presented here *should not* be used in safety-critical situations.

### Safety

The program running on the <ref name="smart_device" /> keeps track of the <ref name="alertee" />'s
location and queries whether the location is contained in one or more currently valid 
<ref name="risk_management#risk_zone" />s.

Depending on the results of the query, the <ref name="risk_status" /> is updated and displayed to
the user.

*The remaining sections intentionally left empty.*
