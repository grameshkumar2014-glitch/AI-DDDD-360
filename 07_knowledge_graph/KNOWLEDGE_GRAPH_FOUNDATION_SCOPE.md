# AI DDDD 360™ — Knowledge Graph Foundation Scope

## 1. Purpose

The Knowledge Graph is the structured scientific relationship layer
of AI DDDD 360™.

It represents validated ontology entities and controlled scientific
relationships while preserving evidence, provenance, uncertainty,
temporal context, conflicting evidence, interpretation, and
reproducibility.

The Knowledge Graph is derived from the validated Step 7 Ontology.

## 2. Authoritative Source

Machine-readable ontology registry:

`06_ontology/ONTOLOGY_REGISTRY.json`

Ontology entity types: **27**

Ontology relationship types: **20**

Ontology registry SHA-256:

`2a51e495a899fe6abc93c17e603af419de0bf8223aab8c1d2a527c003f2cd882`

## 3. Controlled Entity Types

- `Disease`
- `BiologicalProcess`
- `MolecularTarget`
- `Gene`
- `Protein`
- `Pathway`
- `CellType`
- `Tissue`
- `MolecularState`
- `DrugCandidate`
- `DrugModality`
- `Biomarker`
- `PatientSubgroup`
- `DiseaseStage`
- `Evidence`
- `Experiment`
- `ClinicalTrial`
- `SafetyConcept`
- `ADMETConcept`
- `BindingObservation`
- `TargetEngagementObservation`
- `EfficacyObservation`
- `BiologyDeficit`
- `Uncertainty`
- `EvidenceConflict`
- `ExperimentalDesign`
- `InformationGainAssessment`

## 4. Controlled Relationship Types

- `associated_with`
- `expressed_in`
- `located_in`
- `participates_in`
- `regulates`
- `targets`
- `binds`
- `engages`
- `modulates`
- `produces_response`
- `associated_with_disease`
- `supported_by`
- `contradicted_by`
- `derived_from`
- `observed_in`
- `tested_in`
- `has_biomarker`
- `stratified_by`
- `has_uncertainty`
- `has_biology_deficit`

## 5. Knowledge Graph Node Model

Each node represents a validated ontology entity.

The node preserves the ontology entity model, including:

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

## 6. Knowledge Graph Edge Model

Each edge represents one of the 20 controlled ontology relationships.

The edge preserves:

- relationship_id
- relationship_type
- source_entity_id
- target_entity_id
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

## 7. Evidence Safety

The Knowledge Graph preserves the E0-E7 evidence hierarchy.

The system must never silently treat E1 evidence as equivalent to E6
evidence.

## 8. Scientific Interpretation Safety

The Knowledge Graph must distinguish:

- evidence from inference
- hypothesis from demonstrated effect
- binding from efficacy
- supporting evidence from conflicting evidence
- computational prediction from experimental evidence
- uncertainty from established knowledge

## 9. BBE-BD Framework

Bimodality → Binding → Efficacy → Biology Deficit

Binding does not equal efficacy.

The efficacy chain remains:

Target engagement → Pathway modulation → Cellular response →
Disease phenotype → Therapeutic effect

## 10. Provenance and Reproducibility

Graph assertions must preserve sufficient information to determine:

- source
- temporal context
- evidence level
- interpretation
- uncertainty
- conflicting evidence
- human oversight
- reproducibility metadata

## 11. Scope Boundary

Step 8.1 establishes the Knowledge Graph foundation only.

It does NOT yet create:

- a production graph database
- external biomedical data ingestion
- a vector database
- autonomous scientific reasoning
- agent orchestration
- clinical recommendations
- therapeutic recommendations

## 12. Dependency Chain

Step 3 → Step 4 → Step 5 → Step 6 → Step 7 → Step 8

Step 8.1 consumes the validated Step 7 Ontology Registry.

## 13. Validation Requirements

The Knowledge Graph foundation must remain aligned with:

- 27 entity types
- 20 relationship types
- 19 entity attributes
- 17 relationship attributes
- E0-E7 evidence hierarchy
- E1/E6 safety rule
- provenance
- uncertainty
- conflicting evidence
- evidence vs inference
- hypothesis vs demonstrated effect
- human oversight
- reproducibility
- BBE-BD
- binding ≠ efficacy
