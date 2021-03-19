<rasaeco-meta>
{
    "title": "Unique Resource Identification",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "analytics",
            "phase_from": "planning", "phase_to": "construction",
            "level_from": "device/person", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario examines how we can uniquely identify the instances of all the entities in our system.

## Models

*Intentionally left empty.*

## Definitions

<def name="identifier" >

From [Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier):

A Uniform Resource Identifier (URI) is a unique identifier used by web technologies. 
URIs may be used to identify anything, including real-world objects, such as people and places, 
concepts, or information resources such web pages and books.

</def>

## Scenario

Our system supports many non-IFC entities (such as <ref name="risk_management#risk" /> and
<ref name="on-site_logistics#delivery_update" />).

Since we shadow these entities as references in BIM through 
<ref name="evolving_plan#non_ifc_entity" />, they need an <ref name="identifier" />.

We propose the following schema for identification:

```
bimprove://{entity}/{identifier}
```  

The `identifier` in the <ref name="identifier" /> does not have to match the
<ref name="evolving_plan#guid" />. This is important as one part of the system might
not control the other part (or a dependency) so it can not control the identification conflicts.

Here are a couple examples of the <ref name="identifier" />:
* `bimprove://risk/123e4567-e89b-12d3-a456-426614174000` 
* `bimprove://delivery/d67e5a7d-a77c-44bd-b8f7-b860b370c4db`

For example, the fall risk with URI `bimprove://risk/123e4567-e89b-12d3-a456-426614174000`
can be shadowed by `IfcExternalReference` in <modelref name="evolving_plan#bim_extended" />
with a <ref name="evolving_plan#guid" /> set to `52a844ac-3f37-456c-9e86-9e1b905600a7`. 

**Abstraction**.
We abstract the links to these entities from the storage. 

For example, the fall risk might have an REST API accessible through a URL 
`http://some-server.com/risk/123e4567-e89b-12d3-a456-426614174000`.
However, it could also provide a GraphQL interface, direct SQL interface 
 (*e.g.*, `sql://risk/123e4567-e89b-12d3-a456-426614174000`) or some other interface.
 
We consider this to be an implementation detail so that we intentionally decouple how the backend
retrieves or modifies the information about the entity from its identification.


**Recordings**.
The <ref name="digital_reconstruction#recording" /> needs to specify the source and the sensor and 
the accuracy of the sensor:
```
recording://{type of the device}/{identifier of the device}/{identifier of the sensor of the device}/{identifier of the recording}
```

Examples:

```
recording://uxv/ruprechts-uav-3/photo-odometry/7f0d4cad-4a22-4a6d-8f00-10ca08d3e4d4
```

```
recording://manual/some-body/smartphone-camera/89dd9240-d11d-4f79-a7e1-0fe9a5af4d46
```

(Note that we still need to figure this out. 
This is just a first sketch of how we could identify the 
<ref name="digital_reconstruction#recording" />s.)

*The remaining sections intentionally left empty.*
