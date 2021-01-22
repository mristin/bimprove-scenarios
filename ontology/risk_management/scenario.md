<rasaeco-meta>
{
    "title": "Risk Management",
    "contact": "Alberto Palomero <Alberto.Palomero@hrs.ch>, Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Manuel Menendez <manuel.menendez@vias.es>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
        { "target": "uxv_recording", "nature": "focus spots" },
        { "target": "topic_management", "nature": "issues" },
        { "target": "safety_status", "nature": "risk status" }
    ],
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

<def name="preventive_resource">

<level name="zone">This is an <ref name="actor_management#role" /> that is responsible for
one or more <ref name="responsibility_zone" />s on the construction site to keep track and mitigate
the <ref name="risk" />s.</level>

(Mind that a preventive resource and the <ref name="risk_manager" /> can be one and the same
person in certain sites, *e.g.*, when the site is small.)

</def>

<def name="responsibility_zone">

A responsibility zone as an `IfcZone` living in the <modelref name="evolving_plan#bim_extended"/>.

</def>

<def name="assignment">

Responsibility assignment of a <ref name="preventive_resource" />.

The assignment is a non-IFC data structure and relates the <ref name="risk" />s and
the <ref name="preventive_resource" />s.

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

It is tied to zero, one or multiple <ref name="responsibility_zone"/>s.

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

### As-planned

<level name="office">We assume that the data from <modelref name="evolving_plan#bim3d" /> and
<modelref name="evolving_plan#bim_extended" /> is accessible from the office.</level>

**Specification of the <ref name="risk" />s**.
There should be an application so that the <ref name="risk_manager" /> can easily convert 
a <ref name="scheduling#task" /> to a <ref name="risk" /> and capture the additional
information such as the <ref name="risk_zone" />.

There should be also a <ref name="risk" /> management application so that 
the <ref name="risk_manager" /> can also create, list and modify the <ref name="risk" />s (
together with the <ref name="risk_zone" />s, time span *etc.*).

Mind that a <ref name="risk" /> needs not be necessarily associated with a 
<ref name="scheduling#task" />.

<phase name="planning">The <ref name="risk_manager"/> inputs the initial set of 
<ref name="risk"/>s already known during the planning.</phase>

<phase name="construction">Both the <ref name="risk_manager"/> and 
the <ref name="preventive_resource"/> can insert new and change existing 
<ref name="risk"/>s accordingly.</phase>

**Specification of the <ref name="assignment" />s**.
There needs to be a separate application so that the <ref name="risk_manager" /> can create, list 
and modify <ref name="assignment" />s of the <ref name="risk" />s to 
the <ref name="preventive_resource" />s.

Though some <ref name="risk" />s are not necessarily spatially confined 
(*e.g.*, some risks can be abstract, such as "the workers are wearing safety helmets"), 
they are still part of an <ref name="assignment" />.
In these cases, the <ref name="assignment" /> means that a <ref name="preventive_resource" /> is
responsible for the unconfined <ref name="risk" /> in the given zone (*e.g*, that all workers wear a 
helmet in the given zone).

### As-observed

The <ref name="risk_manager" /> needs to create <ref name="uxv_recording#focus_spot" />s in order
to observe the necessary spots for potential new or changed risks.

The <ref name="uxv_recording#focus_spot" />s are observable through 
<ref name="digital_reconstruction#recording" />s and taken into account during the 
<ref name="uxv_recording#mission" />s.

### Divergence

Depending on the <ref name="risk" />, we can use <scenarioref name="thermal_inspection" /> and/or
<scenarioref name="virtual_inspection" /> to inspect whether the risk is present or absent.

For example, the <ref name="preventive_resource" /> can check if the safety nets are still there and
not damaged using <scenarioref name="virtual_inspection" />.
The absent, ill-placed or damaged elements are reported as a 
<ref name="topic_management#topic" /> using <scenarioref name="topic_management" />.

This is different to assessing or discovering a new risk (please see the 
<a href="#section-Safety">Safety section</a>).

### Analytics

The system allows the <ref name="risk_manager" /> to track the following indicators:
* Number of <ref name="topic_management#topic" />s related to escalated <ref name="risk" />s of a
  certain <ref name="risk_type" /> (*e.g.*, as a pre-defined <ref name="topic_management#label" />).

The <ref name="assignment" />s should be visualized separately (*e.g.*, as a 3D or 2D geometry).

### Scheduling

The <ref name="risk_manager" /> needs to inspect the <ref name="scheduling#task" />s
in <scenarioref name="scheduling" /> as the <ref name="scheduling#task_shadow" />s are 
linked to the <ref name="risk" />s.

### Safety

**Virtual inspection.**
The <ref name="risk_manager" /> filters the <ref name="scheduling#task" />s with
an elevated risk in <scenarioref name="virtual_inspection" />.

The spatial and temporal relations between the <ref name="risk_zone" />s are then automatically 
visualized in <scenarioref name="virtual_inspection" /> (*e.g.*, using the temporal validity 
of the <ref name="risk" />).

**Reporting.**
The system needs to report an overview of all the <ref name="risk" />s.

The <ref name="risk" />s need to be displayed together with their  related 
<ref name="scheduling#task" />s, if any, as a time table.

For example, we can display the <ref name="risk" />s as a Gantt diagram.
The <ref name="risk" />s would be represented with thick bars, while the related 
<ref name="scheduling#task" />s would be visualized inside these bigger bars as thin bars.
(Mind that this is just an idea and needs to be experimented with during the implementation.)

The user should filter by:
* <ref name="risk_type" /> (*e.g.*, show only fire risks),
* time range, and
* spatially (by a bounding box, super-zones *etc.*; the spatial filtering takes 
  <ref name="risk_zone" />s into account; there should be a special flag to include/exclude
  unconfined <ref name="risk_zone" />s).

**Escalation.**
If there is a problematic <ref name="scheduling#task" />, 
the <ref name="risk_manager" /> should create a <ref name="topic_management#topic" />.

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
