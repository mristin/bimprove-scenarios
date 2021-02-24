<rasaeco-meta>
{
    "title": "Cost Tracking",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "scheduling", "nature": "inspect over-cost tasks" }
    ],
    "volumetric": [
        {
            "aspect_from": "cost", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario looks into how to track the <ref name="expenditure" />s against the planned
<ref name="cost" />s.

## Models

*The section intentionally left empty.*

## Definitions

<def name="performance_history">

The performance history define a category of <ref name="expenditure" />s based on the life cycle
phase.

It is an `IfcPerfromanceHistory` and lives in <modelref name="evolving_plan#bim_extended" />.

</def>

<def name="expenditure">

Expenditure is an `IfcCostItem` living in <modelref name="evolving_plan#bim_extended" /> together 
with its relations.
In particular, to distinguish it from *estimated* <ref name="cost" />s, expenditures
are explicitly linked to a <ref name="performance_history" /> through `IfcRelAssignsToControl`
(where the performance history is the control and the expenditure the related object).

It can be linked to <ref name="scheduling#task_shadow" />s through GUIDs and 
`IfcRelAssignsToControl` (where the task shadows is the related object). 
See [buildingsmart IFC lexicon on control assingment of IfcCostItem] on an example how cost items 
can be assigned to tasks (and other objects such as elements).

The cost items can be composed, see [buildingsmart IFC lexicon on IfcCostItem].

</def>

<def name="cost">

Cost is an `IfcCostItem` living in <modelref name="evolving_plan#bim_extended" /> representing
an estimated cost.

It can be linked to <ref name="scheduling#task_shadow" />s through GUIDs and 
`IfcRelAssignsToControl` (where the task shadows is the related object). 
See [buildingsmart IFC lexicon on control assingment of IfcCostItem] on an example how cost items 
can be assigned to tasks (and other objects such as elements).

The cost items can be composed, see [buildingsmart IFC lexicon on nesting of IfcCostItem].

</def>

[buildingsmart IFC lexicon on nesting of IfcCostItem]: https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifcsharedmgmtelements/lexical/ifccostitem.htm#object-nesting
[buildingsmart IFC lexicon on control assingment of IfcCostItem]: https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifcsharedmgmtelements/lexical/ifccostitem.htm#control-assignment

<def name="over-cost_task">

An over-cost task is a <ref name="scheduling#task" /> whose sum of related 
<ref name="expenditure" />s are greater than the sum of the related estimated <ref name="cost" />s.

</def>

## Scenario

*The preceding aspect sections intentionally left empty.*

### Cost

Capturing estimating costs is out-of-scope of the BIMProve project.
We rely on third-party platforms to provide us with the data which we shadow
in our system as <ref name="cost" />s.
The external data is imported continuously based on a common format.

Analogously, we rely on a (possibly different) platform for tracking project expenditures.
The expenditure data is continuously imported and shadowed in our system as
<ref name="expenditure" />s.

The relations from both the estimated <ref name="cost" />s and <ref name="expenditure" />s to
<ref name="scheduling#task_shadow" />s need to be encoded in the import data format.

We link both the <ref name="cost" />s and <ref name="expenditure" />s to actual building elements
over <ref name="scheduling#task_shadow" />s.

(At this moment, we still have not decided on the third-party platform for cost planning and
expenditures, so the import details have to be specified later.)

We explicitly do not use a more complex structure involving `IfcWorkPlan` and `IfcCostSchedule`
as these seem too complex to be easily imported from the third-party platforms, while they
bring insufficient additional benefit.

### Analytics

The user should be able to see the <ref name="over-cost_task" />s.
The table should be color coded (*e.g.*, showing <ref name="over-cost_task" />s which are
<10%, 10-20%, 20-50% and >50% over budget).

(At this point, we do not know how the costs will be actually attributed.
It is possible that there are <ref name="cost" />s and <ref name="expenditure" />s which are not
related to a single task or related to multiple tasks.
We have to decide later how we aggregate them appropriately.)

*The remaining aspect sections intentionally left empty.*

## Test Cases

*We still lack comprehensive information on this scenario so the test cases are left out at 
the moment.*

## Acceptance Criteria

*We still lack comprehensive information on this scenario so the acceptance criteria are left out at 
the moment.*
