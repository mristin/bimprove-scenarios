<rasaeco-meta>
{
    "title": "Continuous Plan Update TODO",
    "contact": "Gabor Sziebig <gabor.sziebig@sintef.no>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
    ],
    "volumetric": []
}
</rasaeco-meta>

## TODO

Use external software, feed in only a BCF.

Is it really _only_ BCF?

What about a complete overwrite of the model? 

This has repercussions on uav path planning! 
If BIM updates are official over BCF, these updates will be at low rate. 
But UAVs need to record at much faster rate!
We probably need parallel models: the official one and one for UAVs and other applications.

What happens with consistency with other non-BIM data? 
Ex: Actor deleted, but referenced in extra structures such as delivery and actors.
There can be more data than captured in a single BIM! For example, deliveries or actors. 
But this scenario is only focuses on BIM as the official, legally binding data.

TODO: copy/paste the summary from the confluence, link to the confluence article

What about divergence (as-built vs as-planned) --> 
there are two actions:
1) create the BIM according to the point cloud using the previous plan as a cue.
   This gives a new plan as as-built.
   
2) compare the two plans (reconstructed plan and original plan) 
   --> this is part of visual inspection!
   
So multiple plans are possible: as-digitally-reconstructed and as-planned.

--> This is directly related to digital_reconstruction scenario!!! 

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

