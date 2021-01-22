TODO:
* automatic divergence detection

Examples:
"The power outlet on the 2nd floor in the given room are 10 cm lower, than it should be. 
We need to notify the electrical company to adjust it."
      
"There are 5 pipes instead of 4 on the 2nd floor, it is not an approved change from 
the contractor. This was detected by the automated quality survey."

--> Step 1) detect the divergence using the external software
    Step 2) go to the visual_inspection and examine the element
    
Originally from digital_reconstruction:

<def name="automatic_divergence_detection">

TODO: this is going to the automatic_divergence_detection

The divergence can be detected in two ways:
* Something exists in the <modelref name="plan/main" />, but is missed in the point cloud, or
* Something exists in the point cloud, but is missed in the <modelref name="plan/main" />. 

Implementing to detect these divergences is not part of the BIMprove project, but we rely on
external software such as:
* https://bimandscan.com/autocorr/
* https://www.clearedge3d.com/products/verity/
* https://www.imerso.com/

**Something in BIM, missing in point cloud**.

We assume that each element in the BIM is assigned a time range when it should exist.
(An element can also be destroyed, but still be relevant!)

The relevant elements in BIM need to be marked that we want to automatically check for them.

We use <ref name="point_cloud" /> to check whether there are enough points in the given time range
to support the hypothesis that an object exists.

These checks are done using RANSAC or a similar method and requires further investigation.
(For example, [this paper from ITCon](https://www.itcon.org/paper/2020/11))

This particualr research is part of BIMprove project.

**Something in point cloud, missing in BIM**.

We assume that certain empty spaces are appropriately marked expected to be tidy.

We compute the volume of the "free space" and compare it against the voxel "outliers". 

The competition: 
* https://bimandscan.com/autocorr/
* https://www.clearedge3d.com/products/verity/
* https://www.imerso.com/ (not automatic, only visualization!)

TODO: BIG DECISION: SHOULD WE REALLY COMPETE WITH THEM (except imerso)?

TODO: THIS FEATURE IS BY NATURE SEMI-AUTOMATIC --> the result is an BFC.

</def>

TODO: allow to filter elements from <modelref name="evolving_plan#bim3d" /> by date (by filtering
    the tasks and making the union of all elements referenced by the accepted tasks),
        compare against the selected version of <ref name="digital_reconstruction#as-built" />.
TODO: --> there are also properties that we can not track; for example: is the element painted or
      not --> this would go unnoticed in the divergence detection over time!

TODO: maybe we need to codify the rules to automate a bit the divergence detection as completely 
automatic divergence detection is most probably not feasible due to different tolerances based on
the context?
--> We need to review ITCon 2016 -- a special issue on requirements management for buildings and
    code compliance based on rules and programming languages.
