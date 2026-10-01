# AI DDDD 360(TM) - Ontology Scope

## Step

Step 7 - Ontology

## Purpose

This document defines the controlled scope for the ontology layer
of AI DDDD 360(TM).

The ontology layer provides a controlled semantic representation
of scientific entities, concepts, relationships, identifiers,
evidence references, provenance, and uncertainty required by the
AI DDDD 360(TM) scientific intelligence architecture.

This is a scope specification and not yet a finalized ontology
implementation.

## Scientific Principle

The ontology must preserve the distinction between:

- scientific entities and concepts
- relationships between entities
- evidence supporting relationships
- evidence conflicting with relationships
- evidence provenance
- uncertainty
- inference versus demonstrated effect
- computational evidence versus clinical evidence

The ontology must not silently increase evidence strength.

## Core Ontology Domains

The controlled ontology scope includes the following scientific
domains:

1. Disease and disease biology
2. Biological processes and mechanisms
3. Molecular targets
4. Genes
5. Proteins
6. Pathways
7. Cell types
8. Tissues
9. Molecular states
10. Drug candidates
11. Drug modalities
12. Biomarkers
13. Patient subgroups
14. Disease stages
15. Evidence
16. Experiments
17. Clinical trials
18. Safety and ADMET concepts
19. Binding and target engagement
20. Efficacy and translational concepts
21. Biology Deficits
22. Uncertainty
23. Evidence conflicts
24. Experimental design concepts
25. Information-gain concepts

## Required Ontology Concepts

The ontology must support explicit representation of:

- entity identity
- entity type
- canonical identifier
- alternative identifiers
- source reference
- provenance
- temporal context
- evidence level
- supporting evidence
- conflicting evidence
- uncertainty
- interpretation
- relationship type
- relationship direction where applicable
- evidence versus inference
- hypothesis versus demonstrated effect
- human oversight
- reproducibility metadata

## Evidence Hierarchy

Ontology representations must preserve the AI DDDD 360(TM)
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

## BBE-BD Representation

The ontology must be capable of representing the BBE-BD framework:

Bimodality -> Binding -> Efficacy -> Biology Deficit

Bimodality includes:

- ON/OFF state
- high/low expression
- cell type
- tissue
- disease stage
- patient subgroup
- molecular state

Binding and efficacy must remain distinct.

The efficacy chain must preserve:

Target engagement -> Pathway modulation -> Cellular response
-> Disease phenotype -> Therapeutic effect

Biology Deficit must support unresolved, missing, conflicting,
weak, uncertain, or unsupported mechanistic knowledge.

## Relationship Scope

The ontology scope includes relationships such as:

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

Relationship semantics must remain explicit and traceable.

## Provenance Requirements

Every ontology assertion that represents scientific knowledge
must be capable of retaining provenance sufficient to identify:

- source
- source identifier
- source reference
- temporal cutoff
- evidence level
- interpretation
- limitations
- supporting evidence
- conflicting evidence
- uncertainty

## Safety Requirements

The ontology must inherit the scientific safety requirements
established in the Evidence Model and RAG layers.

The ontology must not:

- convert computational prediction into clinical evidence
- convert binding evidence into demonstrated efficacy
- convert inference into demonstrated effect
- generate unsupported therapeutic conclusions
- discard conflicting evidence
- discard uncertainty
- remove evidence provenance
- bypass human oversight

## Reproducibility

Ontology artifacts must support reproducibility through:

- project version
- ontology version
- source provenance
- temporal cutoff
- artifact identifier
- validation result
- creation timestamp
- relevant Git commit where applicable

## Scope Boundary

This Step 7.2 artifact defines ontology scope only.

It does not yet implement:

- a production ontology
- an ontology database
- a knowledge graph
- external ontology imports
- automated semantic reasoning
- external terminology APIs
- embeddings
- vector databases
- agent orchestration
- LangGraph workflows

Those capabilities remain outside this scope unless explicitly
introduced and validated in later controlled steps.

## Dependency Inheritance

This ontology scope inherits requirements from:

- Step 3 - Scientific Data Model
- Step 4 - Evidence Model
- Step 5 - Data Ingestion
- Step 6 - RAG

The ontology must remain compatible with those completed layers.

## Validation Requirement

Before Step 7 can be closed, the ontology scope and subsequent
ontology artifacts must be validated for:

- completeness
- semantic consistency
- evidence preservation
- provenance preservation
- uncertainty preservation
- supporting/conflicting evidence preservation
- scientific safety
- reproducibility
- deterministic behavior where applicable
- traceability to the Master Control

## Status

Step 7.2 scope specification.

## Created

2026-10-01T03:19:05.523491+00:00
