<rasaeco-meta>
{
    "title": "Virtual Inspection TODO",
    "contact": "TODO",
    "relations": [
    ],
    "volumetric": []
}
</rasaeco-meta>

## TODO

gather it first, then possibly break it up.

### General overview

Different viewers (as applications!)
* Property owner inspection
* Civil engineer inspection
* BIM Manager inspection
* Site Manager inspection

Actions: view, comment, create issue (linked to none, one or more elements)

Nobody can edit! Edits are done *via* continuous_plan_update.

### Versioning
Important: the virtual inspection can take time range/versions into account 
(both for plans and for observed images and point cloud!)

Are point clouds grouped by atomic recordings?

Are there manually recorded point clouds?

What about images? The UAV recordings probably give videos (tied to a single atomic recording), 
while manual images are captured by a phone at an arbitrary time point.

Should we be able to visualize BCF as well? And how?

Should we visualize multiple versions of BIM?
Should they be compared on-the-fly?
(See also below as-digitally-reconstructed vs as-planned!)

Repercussions for time & space complexity!! (O(n^2) if we need to pre-compute all the possible diffs.)

### Information about elements

Specify which general information should be displayed
(manufacturer, company/people who built it, company/people who installed it, *etc.*) 
--> log of an element

So far, these are the relations we collected so far:
* relations to tasks (and, transitively, tasks related to workers, installers and other actors)
  "According to today's plan, the wall segment on 1st floor should be finished. 
  The workers were there, but they have not finished. 
  Tomorrow they are working on another site."

* relations to manufacturer
  "The quality survey shows, that the window on the 1st floor at this position is 5 cm larger. 
  We will need to order larger windows if the whole remains the same size."

* relations to contractors
  "There are 5 pipes instead of 4 on the 2nd floor, it is not an approved change from 
  the contractor. This was detected by the automated quality survey." 

* relation to installer
  "The power outlet on the 2ns floor in the given room are 10 cm lower, than it should be. 
  We need to notify the electrical company to adjust it."

Many of the actors and tasks in the logs are probably not captured in BIM!
--> maybe we need just a free-form log? With individual access levels per nugget of information?

### As-digitally-reconstructed vs as-planned

How do we visualize as-digitally-reconstructed vs as-planned? 
How to highlight the differences? Animation (show one, show the other)?
Over the point cloud & images?

Can we have an external solution compare as-digitally-reconstructed and as-planned and export
a BFC which can be imported and applied *via* continuous_plan_update?

Visualization is one thing (achievable), while computing divergence seems to me (Marko) 
unachievable in this project.

### Visualization of notes

How do we visualize the issues? With an icon displayed on elements linked to an issue?

How is an issue captured in BIM? Or are issues kept in a separate model and linked to BIM elements?

The issues are probably more dynamic than the official BIM update *via* BCF!
--> We need to specify this well!

Or there might be different levels of notes:
* Official issues, need to be officially signed off
* Important notes
* Comments

--> Get feedback from the professionals!

## Summary


## Models


## Definitions


## Scenario

### As-planned


### As-observed


### Divergence


### Analytics


### Scheduling


### Safety


## Test Cases


## Acceptance Criteria

