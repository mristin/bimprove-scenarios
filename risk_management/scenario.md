<rasaeco-meta>
{
    "title": "Risk Management",
    "contact": "Alberto Palomero <Alberto.Palomero@hrs.ch>, Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Manuel Menendez <manuel.menendez@vias.es>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "scheduling",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "safety", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenarios examines how the <ref name="risk" />s should be managed on a construction site.

This involves both keeping track of the existing <ref name="risk" />s as well as inspecting the site
for the new <ref name="risk" />s, checking the state of the installations *etc.*

## Models

<model name="standard/risk_level">

Risk levels defined at the national and international level.

</model>

<model name="risks">

This model captures all the <ref name="risk" />s.

As <ref name="risk" /> is a non-IFC entity, it does not live in 
<modelref name="evolving_plan#bim_extended" />.

</model>

## Definitions

<def name="risk_manager">

<level name="site">This is an <ref name="actor_management#role" /> that manages certain kinds 
of <ref name="risk" />s.</level>

For example, this can be a <ref name="fall_risk#health_and_safety_manager" /> monitoring 
the <ref name="fall_risk#fall_risk" />s or <ref name="fire_risk#site_protection_manager" /> 
monitoring the <ref name="fire_risk#fire_risk" />, but can also be a construction engineer 
responsible for curing the concrete *etc.*

</def>

<def name="risk_level">

This is the risk level according to different standards.

The risk level refers to a concrete standard in <modelref name="standard/risk_level" />.

</def>

<def name="risk_zone">

This is an `IfcZone` living in <modelref name="evolving_plan#bim_extended" /> that demarcates a zone
of a specific <ref name="risk" />.

</def>

<def name="risk_type">

The risk type is a more general type of a risk ("fall", "fire" *etc.*).

</def>

<def name="risk">

A risk is a custom, non-IFC entity representing a safety or an economic risk.

A risk is of a <ref name="risk_type" />.

It is tied to zero, one or multiple <ref name="risk_tracking#responsibility_zone"/>s.

The risk can be associated with zero, one or multiple <ref name="risk_zone" />s.
If there are no <ref name="risk_zone" />s defined, the risk is considered unconfined.
If there is one or more <ref name="risk_zone" />s defined, the risk applies only to these zones.

The risk is also associated with zero, one or more <ref name="scheduling#task" />s. 

The risk must have a validity time span (which can also be open-ended).
There should be a special flag to indicate that the temporal validity of a risk is directly
tied to its corresponding <ref name="scheduling#task" />s.
For example, this is important if the <ref name="scheduling#task" />s are re-scheduled and the risk
temporal validity needs to reflect that.

The risk is assigned a <ref name="risk_level" />.

The risk can be related to one or multiple <ref name="topic_management#topic" />s (*e.g.*,
when a safety-relevant element is missing or damaged).

The risk lives in <modelref name="risks" />s and have 
<ref name="unique_resource_identification#identifier" />.

</def>

## Scenario

In this scenario, we look into how to manage the <ref name="risk" />s with the system.

The <ref name="risk" /> in the context of this scenario does not refer strictly to a safety
risk (such as fall risk or fire risk), but encompasses a much broader family of risks (such as
concrete cracking, which is an economic risk, but not necessarily a safety risk).

This scenario is split into two sub-scenarios by the respective phase:
* <phase name="planning"><scenarioref name="risk_planning" /> which covers how the risk management plan is created during
  the planning,</phase> and
* <phase name="construction"><scenarioref name="risk_tracking" /> which looks into how the risks are
  tracked, mitigated and escalated during the construction.</phase>

### As-planned

<level name="office">We assume that the data from <modelref name="evolving_plan#bim3d" /> and
<modelref name="evolving_plan#bim_extended" /> is accessible from the office.</level>

## Test Cases

<test name="test_for_magnitude">

We write a script to generate automatically dummy tasks.

We also use generated images from <testref name="thermal_inspection#test_for_magnitude" />
to randomly assign them to the dummy tasks.

</test>

<test name="blind_test_removed_item">

(This is a blind experiment and might not be legally possible.)

Remove a safety item and inform the workers.

Check that the responsible person could find out that it is missing using the system. 

</test> 

<test name="analytics_correct_on_an_example">

Record 3 complete states of the whole system and freeze them. 

Manually compute the expected analytics. 

Check that the output of the system coincides with the manually computed analytics.

</test>


## Acceptance Criteria

<acceptance name="magnitude">

The system needs to handle the risk related <ref name="scheduling#task" />s in the
order of thousands.

</acceptance>
