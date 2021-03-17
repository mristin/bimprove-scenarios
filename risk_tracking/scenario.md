<rasaeco-meta>
{
    "title": "Risk Tracking",
    "contact": "Alberto Palomero <Alberto.Palomero@hrs.ch>, Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Manuel Menendez <manuel.menendez@vias.es>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
        { "target": "risk_management", "nature": "in construction" },
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

This scenario is a sub-scenario of <scenarioref name="risk_management" /> which considers
how the risks are tracked, mitigated and escalated on day-to-day basis on the construction
site.

## Definitions

<def name="preventive_resource">

<level name="zone">This is an <ref name="actor_management#role" /> that is responsible for
one or more <ref name="responsibility_zone" />s on the construction site to keep track and mitigate
the <ref name="risk_management#risk" />s.</level>

(Mind that a preventive resource and the <ref name="risk_management#risk_manager" /> can be one and the same
person in certain sites, *e.g.*, when the site is small.)

</def>

<def name="responsibility_zone">

A responsibility zone as an `IfcZone` living in the <modelref name="evolving_plan#bim_extended"/>.

</def>

<def name="assignment">

Responsibility assignment of a <ref name="preventive_resource" />.

The assignment is a non-IFC data structure and relates the <ref name="risk_management#risk" />s and
the <ref name="preventive_resource" />s.

</def>

## Scenario

### As-planned

**Update of the <ref name="risk_management#risk" />s**.
<phase name="construction">Both the <ref name="risk_management#risk_manager"/> and 
the <ref name="preventive_resource"/> can insert new and change existing 
<ref name="risk_management#risk"/>s accordingly.</phase>

**Specification of the <ref name="assignment" />s**.
There needs to be a separate application so that the <ref name="risk_management#risk_manager" /> can create, list 
and modify <ref name="assignment" />s of the <ref name="risk_management#risk" />s to 
the <ref name="preventive_resource" />s.

Though some <ref name="risk_management#risk" />s are not necessarily spatially confined 
(*e.g.*, some risks can be abstract, such as "the workers are wearing safety helmets"), 
they are still part of an <ref name="assignment" />.
In these cases, the <ref name="assignment" /> means that a <ref name="preventive_resource" /> is
responsible for the unconfined <ref name="risk_management#risk" /> in the given zone (*e.g*, that all workers wear a 
helmet in the given zone).

### As-observed

The <ref name="risk_management#risk_manager" /> needs to create <ref name="uxv_recording#focus_spot" />s in order
to observe the necessary spots for potential new or changed risks.

The <ref name="uxv_recording#focus_spot" />s are observable through 
<ref name="digital_reconstruction#recording" />s and taken into account during the 
<ref name="uxv_recording#mission" />s.

### Divergence

Depending on the <ref name="risk_management#risk" />, we can use <scenarioref name="thermal_inspection" /> and/or
<scenarioref name="virtual_inspection" /> to inspect whether the risk is present or absent.

For example, the <ref name="preventive_resource" /> can check if the safety nets are still there and
not damaged using <scenarioref name="virtual_inspection" />.
The absent, ill-placed or damaged elements are reported as a 
<ref name="topic_management#topic" /> using <scenarioref name="topic_management" />.

This is different to assessing or discovering a new risk (please see the 
<a href="#section-Safety">Safety section</a>).

### Analytics

The system allows the <ref name="risk_management#risk_manager" /> to track the following indicators:
* Number of <ref name="topic_management#topic" />s related to escalated <ref name="risk_management#risk" />s of a
  certain <ref name="risk_management#risk_type" /> (*e.g.*, as a pre-defined <ref name="topic_management#label" />).

The <ref name="assignment" />s should be visualized separately (*e.g.*, as a 3D or 2D geometry).

### Scheduling

The <ref name="risk_management#risk_manager" /> needs to inspect the <ref name="scheduling#task" />s
in <scenarioref name="scheduling" /> as the <ref name="scheduling#task_shadow" />s are 
linked to the <ref name="risk_management#risk" />s.

### Safety

**Virtual inspection.**
The <ref name="risk_management#risk_manager" /> filters the <ref name="scheduling#task" />s with
an elevated risk in <scenarioref name="virtual_inspection" />.

The spatial and temporal relations between the <ref name="risk_management#risk_zone" />s are then automatically 
visualized in <scenarioref name="virtual_inspection" /> (*e.g.*, using the temporal validity 
of the <ref name="risk_management#risk" />).

**Reporting.**
The system needs to report an overview of all the <ref name="risk_management#risk" />s.

The <ref name="risk_management#risk" />s need to be displayed together with their related 
<ref name="scheduling#task" />s, if any, as a time table.

For example, we can display the <ref name="risk_management#risk" />s as a Gantt diagram.
The <ref name="risk_management#risk" />s would be represented with thick bars, while the related 
<ref name="scheduling#task" />s would be visualized inside these bigger bars as thin bars.
(Mind that this is just an idea and needs to be experimented with during the implementation.)

The user should filter by:
* <ref name="risk_management#risk_type" /> (*e.g.*, show only fire risks),
* time range, and
* spatially (by a bounding box, super-zones *etc.*; the spatial filtering takes 
  <ref name="risk_management#risk_zone" />s into account; there should be a special flag to include/exclude
  unconfined <ref name="risk_management#risk_zone" />s).

**Escalation.**
If there is a problematic <ref name="scheduling#task" />, 
the <ref name="risk_management#risk_manager" /> should create a <ref name="topic_management#topic" />.
