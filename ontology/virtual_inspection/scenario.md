<rasaeco-meta>
{
    "title": "Virtual Inspection",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "topic_management", "nature": "issues" }
    ],
    "volumetric": [
       {
            "aspect_from": "as-planned", "aspect_to": "divergence",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "office"
       }
    ]
}
</rasaeco-meta>

## Summary

This scenario is about manual virtual inspections of 
<level name="site">the construction site</level> usually from the 
<level name="office">site office</level>

## Models

*Intentionally left empty.*

## Definitions

*Intentionally left empty.*

## Scenario

The inspection is based on:
* the geometry of the <modelref name="evolving_plan#bim3d" />
* the observations (such as <modelref name="digital_reconstruction#images" /> or
  <modelref name="digital_reconstruction#as-built" />),
* the relations to abstract entities (such as tasks, costs *etc.*) from 
  <modelref name="evolving_plan#bim_extended" />, and
* the <ref name="topic_management#topic" />s.

The data is visualized as a 3D model.

### As-planned

**Visualization**.
The system displays a selected <ref name="evolving_plan#revision" /> of 
<modelref name="evolving_plan#bim3d" />.

Two <ref name="evolving_plan#revision" />s can be compared visually, *e.g.*, by using color 
tainting. (Mind that the difference between the two models is not computed explicitly, only 
demonstrated visually.)

**Filtering of the displayed elements**.
The elements can be filtered by a set of one or more <ref name="evolving_plan#guid" />s or 
unique resource identifiers (URIs).
 
The elements can be further filtered by the type and and property values.

To spatially and logically filter elements, a bounding box, a set of related zones and/or a set
of related groups can be selected.

Furthermore, we can also filter the elements by the related <ref name="scheduling#task_shadow" />s.

The <ref name="scheduling#task_shadow" />s can be filtered by time range, task type and/or
a set of related <ref name="actor_management#actor" />s (manually picked).
The filtering of tasks dictates the filtering of displayed elements. 

The element can be further filtered by a set of related <ref name="topic_management#topic" />s.
The <ref name="topic_management#topic" />s can be filtered by a priority, filter, status and time
range.

All these filters can be combined to compositional filters as intersections and/or unions
of filters.

Note that the filtering is also relevant for other components of the system so that they can link 
to virtual inspection.
This implies that the query underlying the filtering should be representable as a string and can be
easily embedded in an an URL.

The hidden elements can either be completely hidden or displayed as markedly transparent.

(Note about the implementation priorities:
it remains to be seen during the implementation what queries are ergonomic and what can be 
practically implemented.
We need to start with a simple solution and progress to the more sophisticated ones.

Please also consider the remark regarding the importance of filtering when inspecting the
divergence between the plans and as-built observations.)

**Risk zone visualization**.
The <ref name="risk_management#risk_zone" />s are a special kind of zones and need proper 
visualization.

For example, they can be coloured appropriately by their <ref name="risk_management#risk_level" />.

We also need to take into account the temporal validity of a risk zone (*e.g.*, see 
<ref name="risk_management#risk" />).

The user can turn these zone visualizations on/off.

This visualization is particularly useful for the briefing sessions.

**Topic visualization**.
We visualize all the related <ref name="topic_management#topic" />s 
of the elements currently in the view (*e.g.*, as icons). 
You can follow the link straight to <scenarioref name="topic_management" /> to read about that 
<ref name="topic_management#topic" />.

You can also filter the visualized <ref name="topic_management#topic" />s by setting 
a priority filter, status (open, candidate, resolved, +user defined *etc.*) and time range.
Mind that this is different from filtering the *elements by filtering their related topics*. 

Visualizing the content of a <ref name="topic_management#topic" /> is out-of-scope of the project.
We deem such a visualization to be confusing. 
We expect the user to use <scenarioref name="topic_management" /> for general topic management.
TODO: link to divergence_detection for how to create a topic when as-built and bim3d diverge. 

**<ref name="topic_management#viewquery" /> creation**.
To create a <ref name="topic_management#viewquery" />, the user needs to filter in the
relevant data (as-planned, as-observed and divergence).

The user is provided a special GUI element to convert the query into
an <ref name="topic_management#viewquery" />, preview it and attach it as 
a <ref name="topic_management#comment" /> to a <ref name="topic_management#topic" />.

**Information about an element.**
An individual BIM element can be selected (*e.g.*, by clicking on it).

The information about the element is displayed based on the extended information from 
<modelref name="evolving_plan#bim_extended" />.
This include relations of an element to actors, tasks, costs *etc.*

Once the relations are displayed, we can follow the reference of, say, a related`IfcTask` and 
jump to <scenarioref name="scheduling" />.

Additionally, we list all the <ref name="topic_management#topic" />s (and, consequently, to 
<ref name="topic_management#comment" />s) involved with the element.
The user can jump to the <scenarioref name="topic_management" /> to see the details.

**Access**.
We do not distinguish the relations in different access categories. 
The user is either allowed to see all the relations *OR* 
she is not allowed to see any (in which case, she sees only the geometry and the point clouds).

### As-observed

**Observed uninterpretable geometry**.
The user can select what observations should be displayed:
* points from <modelref name="digital_reconstruction#point_cloud" />,
* voxels from <modelref name="digital_reconstruction#voxel_cloud" /> or
* reconstructed geometry from 
  <modelref name="digital_reconstruction#reconstructed_geometry" />.
  
These observations can be filtered by:
* time range,
* the source (*e.g.*, <ref name="uxv_recording#UXV" />s and 
  the related <ref name="uxv_recording#sensor" />s, 
  manual snapshot filtered by the relevant <ref name="actor_management#actor" />s *etc.*),
* bounding box, and
* selected BIM element(s)
  (*e.g.*, by selecting the bounding box over the elements and enlarging it a bit).

The system should be able to display multiple overlapping observations.
They can be differentiated by color tainting related to a selection of multiple time ranges. 
For example, the points corresponding to the time range 12:00-16:00 2021-01-13 are tainted red,
and the points corresponding to the time range 00:00-23:59 2021-01-05 are tainted blue.

**Images**.
Images are displayed as icons anchored at their position.

The user can view individual images (*e.g.*, by clicking on their icon).

The user can filter the images similar to the point cloud:
* by selecting individual images,
* by selecting one or more BIM elements (so that all images capturing the elements will be
  selected whereas the visibility is defined through 
  <modelref name="digital_reconstruction#as-built" />),
* time range,
* type of image (RGB, thermal *etc.*),
* ... and many more criteria (to be discussed during the implementation). 

The <ref name="thermal_inspection#thermal_image" />s are a special case where we want to include 
semantic information about the temperature.
Instead of displaying a general icon, we want to summarize the temperature.
For example, we could show minimum, 10%-quantile, 90%-quantile and maximum as a rectangle.
(How we display this information is to be decided during the implementation.)  

**As-built**.
Additionally, the user can display the geometry corresponding to a version of  
<modelref name="digital_reconstruction#as-built" />.
The user can also visually compare two different as-built versions (*e.g.*, by color tainting).

The filtering functionality is same as filtering the as-planned elements.  

### Divergence

The as-planned and as-observed views can be merged in a single one by stacking.

If both <modelref name="evolving_plan#bim3d" /> and 
<modelref name="digital_reconstruction#as-built" /> are to be displayed,
we visually compare them, *e.g.*, by color tainting to highlight the one or the other.

Since the elements in <modelref name="digital_reconstruction#as-built" /> share
the identifiers with <modelref name="evolving_plan#bim3d" />, we can also apply the same filtering
mechanism as for as-planned elements.

The rich filtering capabilities are particularly relevant for the visualization of the as-built
*versus* as-planned differences. While their benefit is rather marginal during inspection
of as-planned elements, it becomes much more difficult to spot important deviations without
proper focus on different kinds of elements as not all deviations are equal.

For example, the deviation of 1cm might be acceptable for one wall, but unacceptable for another or 
for the width of a window frame. Where elements need to be inspected manually, showing only the
relevant subset (both the planned elements as well as their observations) is crucial. 

We also need to provide a functionality to manually measure distances.
For example, this can be related to <scenarioref name="risk_management" /> where we need to check
that emergency exits are close enough. 
Another example is to verify manually if a building element has been properly constructed. 

**Example**.
We examine the following story.

"The quality survey shows, that the window on the 1st floor at this position is 5 cm larger. 
We will need to order larger windows if the whole remains the same size."

Here are the steps how this story can be effectuated using virtual inspection:
1) Select the latest <ref name="evolving_plan#revision" /> of 
   <modelref name="evolving_plan#bim3d" />. 
   
   Filter the elements by the desired date (to hide all the irrelevant elements from 
   <modelref name="evolving_plan#bim3d" />).
2) Select the time range to include the relevant recording(s).
3) Navigate to the element in question.
4) Examine the element comparing the as-planned geometry from 
   <modelref name="evolving_plan#bim3d" /> with the point cloud, voxel cloud, 
   reconstructed geometry and/or images (filtered by the appropriate time range) and 
   as-built geometry (selected by the appropriate version).
5) Select the element to see its relations.
6) Go through its relations to tasks and search for the task corresponding to the installation.
7) Follow the reference to see the details of the task and finally retrieve 
   the relationship to the installer.
8) Create a new <ref name="topic_management#topic" /> describing the order and tracking 
   further steps.

(As it might be obvious from this example, we still need to figure out how filtering can be 
made ergonomic.
For example, it might make sense to pick a single time range and have it applied both to filtering
elements in <modelref name="evolving_plan#bim3d" /> by filtering tasks, to select the appropriate 
version of <modelref name="digital_reconstruction#as-built" /> and to filter the images, point cloud
and other observations.

We need to experiment with the filtering during the implementation. We know for now that the 
backend should provide a versatile query mechanism.)

### Analytics

*Intentionally left empty.*

### Scheduling

*Intentionally left empty.*

### Safety

*Intentionally left empty.*

## Test Cases

TODO: discuss with Dag

## Acceptance Criteria

TODO: discuss with Dag what machine should be expected (as a reference configuration to be tested against); 
    what about the volume of the point cloud, BIM etc.?