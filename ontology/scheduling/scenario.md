<rasaeco-meta>
{
    "title": "Scheduling",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>, Oyvind Kjollesdal <oyvind.kjollesdal@afgruppen.no>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
        { "target": "evolving_plan", "nature": "task shadows" }
    ],
    "volumetric": [
        {
            "aspect_from": "scheduling", "aspect_to": "scheduling",
            "phase_from": "planning", "phase_to": "construction",
            "level_from": "site", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

The <ref name="scheduler" />s do not want to use BIMprove system for scheduling and planning.
This scenario therefore looks into how we integrate with the external solutions.

## Models

<model name="last_planner_data">

This is the model containing all the <ref name="last_planner_task" />s accessible
through the external <ref name="last_planner_system" />.

</model>

## Definitions

<def name="scheduler">

The scheduler plans the construction.

</def>

<def name="phase_plan">

A legally binding coarse long-term plan.

</def>

<def name="last_planner_system">

The software solution for managing lean construction.

Note that the [last planner system](https://en.wikipedia.org/wiki/Lean_construction#Last_Planner_System)
can also refer to a planning system.
In this document, we use the term to refer to a *software system*, not a planning system.

</def>

<def name="task">

Piece of work that needs to be scheduled.

It is represented as <ref name="last_planner_task" /> in <modelref name="last_planner_data" />, and
as a <ref name="task_shadow" /> in <modelref name="evolving_plan#bim_extended" />.

</def>

<def name="last_planner_task">

A <ref name="task" /> managed by a <ref name="last_planner_system" /> and living in
<modelref name="last_planner_data" />.

</def>

<def name="task_shadow">

Task shadow is an `IfcTask` living in the <modelref name="evolving_plan#bim_extended" /> shadowing
the <ref name="last_planner_task" />.

</def>

## Scenario

*The preceding aspect sections intentionally left empty.*

### Scheduling

The <ref name="scheduler" />s do not want to use BIMprove system for scheduling and explicitly
want to rely on external tools.
This scenario therefore looks into how we integrate with the external solutions.

Notably, we do not aim to integrate with solutions for long-term coarse planning
(a.k.a. <ref name="phase_plan" />).
Such solutions include [Synchro](https://www.youtube.com/watch?v=sX0NUKDJ3b4),
Microsoft Project, Primavera and others.
The <ref name="phase_plan" />s are legally binding and change only very infrequently,
if ever, during the project.
As they are not updated frequently enough, we can not use them as a reliable source for the time
dimension.

Instead of <ref name="phase_plan" />s, we focus on the short-term plans managed by the
<ref name="last_planner_system" />s.

We focus only on a single <ref name="last_planner_system" />, [Visilean](http://www.visilean.com),
but we can integrate with other solutions later (*e.g.*, Synchro, Microsoft Project, Houly and
TouchPlan).

As the scheduling is done outside of BIMprove, we explicitly do *not* provide re-scheduling
functionality.
It is a non-goal to develop a last planner system.
In the same line, we do not develop analytics and obstacle and delay analysis for the
<ref name="task" />s.
This is part of the external <ref name="last_planner_system" />.

**Importing**.
We only help the progress monitoring and import the scheduling information from the external
parties to link it with the elements in <modelref name="evolving_plan#bim3d" /> and
<modelref name="evolving_plan#bim_extended" />.

In order to model the <ref name="task" />s, we have to create <ref name="task_shadow" />s and
their relationships, as well as map the references to actors and building elements from the
<ref name="last_planner_system" /> to <modelref name="evolving_plan#bim_extended" />.

The data in <modelref name="last_planner_data" /> needs to be imported continuously into
<modelref name="evolving_plan#bim_extended" /> (*via* triggers, polling or manual export/import,
depending on what is available).

The import workflow from <modelref name="last_planner_data" /> to
<modelref name="evolving_plan#bim_extended" /> follows the steps:
* Create/update the <ref name="task_shadow" />s for all the <ref name="last_planner_task" />s
    * Parse the <ref name="last_planner_task" /> either directly (if possible,
      depending on the export format) or using structured text in the body
* Map the <ref name="actor_management#actor" />s
* Map the references to building elements
* Create/update the shadows for all the relationships between the <ref name="task" />s and
  <ref name="actor_management#actor" />s

Mind that the system should not completely overwrite the relevant data in
<modelref name="evolving_plan#bim_extended" />, but extend it.
This means that we assume the <ref name="evolving_plan#guid" />s to be stable throughout the
project. (It is also tricky to handle the deletions, which is left as an important implementation
detail.)

If the <ref name="last_planner_system" /> does not provide a mechanism to explicitly link to
building elements, <ref name="actor_management#actor" /> and the relationships, we extract this
information from the structured text of the <ref name="last_planner_task" /> body
(*e.g.*, from the footer, similar to
[git trailers](https://git.wiki.kernel.org/index.php/CommitMessageConventions)).

For example, we can use <ref name="evolving_plan#guid" /> and `Related elements:` to structure
the references to the building elements:

```
Related elements:
f6b569e9-beb8-42e7-a44e-4213b92ffb22,
b5e9a2b8-687e-4f5e-a34f-c0fd42768672,
f0ee91a0-d423-4c65-8c01-0c5ba842f9a6
```

(Alternatively, we might use URLs, URIs *etc.* We leave the representation as an important
implementation detail.)

We can also specify some of the properties of a <ref name="task" />.
For example, to specify the task type (`PredefinedType`), we can write in
the body of the <ref name="last_planner_task" />:

```
PredefinedType: CONSTRUCTION
```

**Visualization**.
As the planning is done by the external <ref name="last_planner_system" />, we do not aim for
a sophisticated visualization.

The system should provide basic browsing experience so that other parts of the system can
link to the <ref name="task" /> to show further details.

BIMprove system should be able to:
* Show the list of the <ref name="task" />s,
* Show the detail information about the <ref name="task" /> and its relationships to actors and
  elements, and
* Display the timeline (nice-to-have)

For example, showing the detailed information is important so that the user can get the detailed
information about a <ref name="task" /> coming from <scenarioref name="virtual_inspection" />.

**Risks**.
We need to visualize the <ref name="risk_management#risk" />s (such as fall or fire risks)
related to the <ref name="task" />s.

The user should be able to follow through to examine the risk in more detail in the
specific application through a <ref name="unique_resource_identification#identifier" />.

**Task to topic**.
The user should be provided the interface to translate a <ref name="task_shadow" /> to a
<ref name="topic_management#topic" />.
Since the <ref name="task_shadow" />s are read-only, the additional information (such as
references to BIMprove-specific entities) about the <ref name="task" /> can only be included in
the <ref name="topic_management#topic" />, but can not be fed back
to the <ref name="last_planner_system" />.

There are also more structured options available in the system.
For example, a delivery task can be automatically converted to
<ref name="logistics#delivery" /> as a <ref name="topic_management#topic" />
(see <scenarioref name="logistics" />).

**Closing of <ref name="task" />s**.
Since we do not control the <ref name="last_planner_task" />s (we only import them),
we can not close the <ref name="task" />s automatically.

The user or the system should be able to convert a <ref name="last_planner_task" /> into a
<ref name="topic_management#topic" /> and keep track of its status using
<ref name="topic_management#comment" />s.

In many cases, if the system is tracking the status and not the user, we use structured
<ref name="topic_management#comment" />s.
For example, the task corresponding to a <ref name="logistics#delivery" /> is converted to a
<ref name="topic_management#topic" />.
So when the delivery is terminated, we can close the <ref name="topic_management#topic" />
(which we control), but we can only notify the <ref name="scheduler" />.
The <ref name="scheduler" /> needs to close the corresponding <ref name="last_planner_task" />
in the <ref name="last_planner_system" /> manually.

We emphasize here that there is only a
[unidirectional data flow](https://en.wikipedia.org/wiki/Unidirectional_Data_Flow_(computer_science)):
1) <ref name="last_planner_task" /> to
2) <ref name="task_shadow" /> (*via* synchronization) to
3) <ref name="logistics#delivery" /> (*via* conversion) to
4) delivery closed (*via* <ref name="logistics#delivery_update" />) to
5) <ref name="last_planner_task" /> closed (manually *via* <ref name="last_planner_system" />) to
6) <ref name="task_shadow" /> closed (*via* synchronization).

Perhaps we can have special <ref name="topic_management#topic" />s which we can directly link to
closing of the tasks and feed-back the closing to the last planner system, but this remains to be
seen at the implementation.

*The remaining aspect sections intentionally left empty.*

## Test Cases

<test name="manual_import">

The system can import a sample file as exported by a <ref name="last_planner_system" />.

</test>

<test name="live_import">

We create a dummy account on the <ref name="last_planner_system" />.

We script the <ref name="last_planner_system" /> actions
(*e.g.* using [Selenium](https://www.selenium.dev/)) to create a couple of tasks.

The system should import them as <ref name="task_shadow" />s.

We script the deletion and addition of a couple of more tasks.

The <ref name="last_planner_task" />s should be shadowed appropriately.

</test>

<test name="magnitude">

Similar to <testref name="live_import" />, we create a dummy account on the
<ref name="last_planner_system" />.

We script the <ref name="last_planner_system" /> to create the <ref name="last_planner_task" />s of
the magnitude in <acceptanceref name="magnitude" />.

</test>

## Acceptance Criteria

<acceptance name="magnitude">

We need to handle thousands of <ref name="last_planner_task" />s and thousands of
<ref name="actor_management#actor" />s.

</acceptance>
