### Analysis Package Elements _(DRAFT)_
This document lists and describes the elements required for an analysis package. Here, an element is defined as categorical information needed to build, understand and use the package in a traceable and repeatable manner. Each element needs to be present in the package's code and supporting documents. All the elements listed below are required for each stage of the analysis package life cycle: design, development, review, acceptance, deployment, maintenance, and curation. Each element, with its provenance, **must** be present in that package's bapcat record.

This document is derived from <https://github.com/usgs-bcb/documenting-baps/blob/master/analysis-package-elements.md> and <https://github.com/usgs-bis/nbmdocs/blob/master/docs/baps.rst> (Retrieved 2019-12-10).

#### Purpose
Describe the purpose of the analysis package at a level of detail sufficient for the casual reader to assess the applicability of the package to their work. In summary form, document what the analysis is designed to do and how it does it. Provide the basis for the analysis. List at least one stakeholder for the analysis package. Summarize the outputs.

As an example, look at "Protection Status of Ecological Systems by Ecoregion", one of the BAPs deployed to production at <https://maps.usgs.gov/biogeography>. Clicking on the Protection Status of Ecological Systems by Ecoregion BAP's blue and white information "i" pulls this information from ScienceBase from the BAP's ScienceBase item:
> This provisional Biogeographic Analysis Package provides an analysis of protection status for ecological systems within Omernik Level III Ecoregions.  The ecological system classification defines groups of plant communities that tend to co-occur within landscapes with similar ecological processes, substrates, and/or environmental gradients and is the primary map class used in the Gap Analysis Program (GAP) land cover layer (based on 2001 satellite imagery).  This package can be used to identify the ecoregions where ecological systems have the greatest representation in GAP Status 1 and 2 lands (lands managed for the protection of biodiversity) and the ecoregions where ecological systems are the least protected.

> One important use of the data in this Biogeographic Analysis Package is to evaluate what proportion of the ecological systems in an ecoregion are managed for long-term conservation. These data can be expressed as “threshold” levels of ecological system protection. These thresholds provide a convenient reporting framework ... (<https://www.sciencebase.gov/catalog/item/5645fa07e4b0e2669b30f267>, retrieved 2018-02-20)

*Required provenance values:*

#### Authors
Provide an inclusive list of the people who created the analysis package. Document their full name and associated organization at the time the analysis package is produced. Identify the point of contact.

*Required provenance values:*

#### Stakeholders
Identify and document the people and communities that have a stake in the development and use of the analytical capabilities of the package. Ideally, these stakeholders are actively involved in decision making processes related to biogeographic and ecological synthesis activities or conservation management. Stakeholder work with the package authors to define the purpose, layout the analytical logic, identify the inputs and outputs, provide test data for verification and validation, and provide critcal feedback.

Where possible, each analysis package will be associated with a real person that represents a recognized or definable community. As discussed in the bst.rst document (<https://github.com/usgs-bis/nbmdocs/blob/master/docs/baps.rst> (retrieved 2019-12-10), we call this named person the Actual Stakeholder.

There will be times when we are unable to identify an Actual Stakholder or times when that person does not want to be tagged as such. In these  cases, identify and, to the extent possble, document an Abstract Stakeholder or a persona that may incorporate the analytical results into their decision making process.

*Required provenance values:*

#### Inputs
Document all inputs. Names, links, security constraints, spatial extent and resolution, temporal extent and resolution, example code to access are all important to capture. Documenting these early on makes it easier for others to jump in and help debug, capture the provenance and, later in the process, are critical to the developers operationalizing the scientific code. A clear enumeration of the inputs helps users assess the applicability of the package to their analytical needs.

*Required provenance values:*

#### Outputs
Document all outputs. Again names, links, security constraints, spatial extent and resolution, temporal extent and resolution, example output code all help speed development and ensure repeatability.

*Required provenance values:*

#### Constraints
List and adequately explain analytical constraints. For example, is the analysis only appropriate at a certain spatial scale or resolution? Are there temporal aspects that must be met for a valid analysis? What conditions need to be met before performing a given analysis?

*Required provenance values:*

#### Dependencies
List all dependencies. Are there specific software libraries, packages, or other BAPs that are required to do this analysis? If so, what are they called, where can they be found and what version was used? This information will also be made available in the package's provenance trace.

*Required provenance values:*

#### Code
Document the code. Be aware of and try to code against APIs and standards (e.g. W3C and OGC). Follow USGS best practices for code development. Code used to produce and maintain analysis packages must be under source control in a publically accessible repository. Provide links to the repository or repositories used.

*Required provenance values:*

#### Tests
Provide tests and test data for the analysis package code. Document the purpose for the tests and the expected results. Store test code and data in the same publically accessible repository as the source code. Provide links.

*Required provenance values:*

#### Citations
Provide the citations necessary to establish the scholarly basis for the choice of analytical methodology and implementation and the necessay background users need to understand and use the BAP for their own work.

*Required provenance values:*

#### Provenance
Traceable and transparent provenance information is required for each element listed above.
