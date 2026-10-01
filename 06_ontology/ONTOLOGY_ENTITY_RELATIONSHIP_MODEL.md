# AI DDDD 360(TM) - Ontology Entity and Relationship Model

## Step

Step 7.4 - Ontology Entity and Relationship Model

## Purpose

This document defines the controlled entity and relationship model
for the AI DDDD 360(TM) ontology layer.

It specifies the semantic structures required to represent
scientific entities, relationships, evidence, provenance,
uncertainty, and scientific interpretation.

This artifact is a model specification only.

## Entity Model

Every ontology entity must support the following core attributes:

- entity_id
- entity_type
- canonical_name
- canonical_identifier
- alternative_identifiers
- description
- source_reference
- provenance
- temporal_context
- evidence_level
- interpretation
- limitations
- uncertainty
- supporting_evidence
- conflicting_evidence
- evidence_vs_inference
- hypothesis_vs_demonstrated_effect
- human_oversight
- reproducibility_metadata

## Core Entity Types

The controlled entity types are:

1. Disease
2. BiologicalProcess
3. MolecularTarget
4. Gene
5. Protein
6. Pathway
7. CellType
8. Tissue
9. MolecularState
10. DrugCandidate
11. DrugModality
12. Biomarker
13. PatientSubgroup
14. DiseaseStage
15. Evidence
16. Experiment
17. ClinicalTrial
18. SafetyConcept
19. ADMETConcept
20. BindingObservation
21. TargetEngagementObservation
22. EfficacyObservation
23. BiologyDeficit
24. Uncertainty
25. EvidenceConflict
26. ExperimentalDesign
27. InformationGainAssessment

## Relationship Model

Every ontology relationship must support:

- relationship_id
- subject_entity_id
- relationship_type
- object_entity_id
- source_reference
- provenance
- temporal_context
- evidence_level
- interpretation
- limitations
- uncertainty
- supporting_evidence
- conflicting_evidence
- evidence_vs_inference
- hypothesis_vs_demonstrated_effect
- human_oversight
- reproducibility_metadata

## Controlled Relationship Types

The initial controlled relationship vocabulary includes:

- associated_with
- expressed_in
- located_in
- participates_in
- regulates
- targets
- binds
- engages
- modulates
- produces_response
- associated_with_disease
- supported_by
- contradicted_by
- derived_from
- observed_in
- tested_in
- has_biomarker
- stratified_by
- has_uncertainty
- has_biology_deficit

## Relationship Semantics

### Disease Biology

Disease may be associated_with biological processes,
molecular targets, pathways, cell types, tissues,
molecular states, biomarkers, and disease stages.

### Target Relationships

A drug candidate may target a molecular target.

A drug candidate may bind a molecular target.

Binding must not automatically imply efficacy.

### Target Engagement

Target engagement must be represented separately from binding
where the evidence supports the distinction.

### Efficacy

Efficacy must preserve the following chain:

Target engagement
-> Pathway modulation
-> Cellular response
-> Disease phenotype
-> Therapeutic effect

Each stage must remain independently representable.

### Biology Deficit

A BiologyDeficit entity may represent:

- missing knowledge
- conflicting evidence
- weak evidence
- uncertain evidence
- unsupported mechanistic assumptions
- unresolved biological mechanism

## Evidence Representation

Evidence is a first-class ontology entity.

Each Evidence entity must preserve the AI DDDD 360(TM)
evidence hierarchy:

- E0 - No evidence
- E1 - Computational prediction
- E2 - Molecular / biochemical evidence
- E3 - Cellular evidence
- E4 - Animal / preclinical evidence
- E5 - Human observational evidence
- E6 - Clinical trial evidence
- E7 - Regulatory / validated clinical evidence

The ontology must never silently treat E1 evidence as equivalent
to E6 evidence.

## Evidence Relationships

Evidence may:

- support an entity or relationship
- contradict an entity or relationship
- be derived_from another source
- be observed_in an experiment
- be tested_in a clinical trial

Supporting and conflicting evidence must remain separately
representable.

## Provenance Model

Every scientific assertion must retain provenance sufficient to
identify:

- source
- source identifier
- source reference
- temporal cutoff
- capture context
- evidence level
- interpretation
- limitations

## Uncertainty Model

Uncertainty must be explicitly representable.

An uncertainty assertion must be capable of identifying:

- uncertainty_id
- uncertainty_type
- affected_entity_or_relationship
- description
- evidence_basis
- severity_or_importance
- supporting_evidence
- conflicting_evidence
- temporal_context
- provenance

The ontology must not silently convert uncertainty into certainty.

## BBE-BD Representation

The ontology must represent:

Bimodality
-> Binding
-> Efficacy
-> Biology Deficit

Bimodality may include:

- ON/OFF state
- high/low expression
- cell type
- tissue
- disease stage
- patient subgroup
- molecular state

Binding, target engagement, efficacy, and Biology Deficit
must remain separately representable.

## Scientific Safety

The ontology must not:

- convert computational prediction into clinical evidence
- convert binding into demonstrated efficacy
- convert inference into demonstrated effect
- discard conflicting evidence
- discard uncertainty
- remove provenance
- generate unsupported therapeutic conclusions
- bypass human oversight

## Reproducibility

Ontology entities and relationships must support:

- project version
- ontology version
- source provenance
- temporal cutoff
- artifact identifier
- validation result
- creation timestamp
- Git commit where applicable

## Scope Boundary

This model does not implement:

- production database storage
- knowledge graph execution
- external ontology imports
- automated semantic reasoning
- external terminology services
- embeddings
- vector databases
- agent orchestration
- LangGraph workflows

## Dependency Inheritance

This model inherits requirements from:

- Step 3 - Scientific Data Model
- Step 4 - Evidence Model
- Step 5 - Data Ingestion
- Step 6 - RAG
- Step 7.2 - Ontology Scope

## Validation Requirements

The model must be validated for:

- entity completeness
- relationship completeness
- semantic consistency
- evidence-level preservation
- provenance preservation
- uncertainty preservation
- supporting evidence preservation
- conflicting evidence preservation
- BBE-BD separation
- binding versus efficacy separation
- scientific safety
- reproducibility
- deterministic representation
- traceability

## Status

Step 7.4 model specification.

## Created

2026-10-01T03:22:46.642689+00:00
