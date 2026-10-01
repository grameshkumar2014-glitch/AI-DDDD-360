# AI DDDD 360 - RAG Retrieval Record Model

## Purpose

Define the minimum provenance-preserving record required for retrieved
scientific information.

## Required Scientific Fields

- Evidence level E0-E7
- Source reference
- Source identifier
- Temporal cutoff
- Retrieval query
- Retrieved content reference
- Interpretation
- Limitations
- Supporting evidence
- Conflicting evidence
- Uncertainty
- Evidence versus inference
- Hypothesis versus demonstrated effect

## Reproducibility Fields

- Project version
- Experiment ID
- Model version
- Prompt version
- Context version
- Random seed where applicable
- Evaluation dataset
- Git commit
- Source SHA-256
- Retrieval timestamp
- Results reference

## Scientific Safety

The record must preserve the distinction between computational prediction
and clinical evidence.

The system must not derive a therapeutic conclusion from retrieval alone.

Human oversight is required.

## Evidence Safety

E1 computational evidence must remain distinguishable from E6 clinical
trial evidence.

Supporting and conflicting evidence must remain separately represented.

Uncertainty must not be silently removed.

## Scope Boundary

This model defines a provenance-preserving record structure only.

It does not specify:

- embedding models
- vector databases
- retrieval algorithms
- chunking algorithms
- ranking algorithms
- external databases
- external APIs
