# AI DDDD 360 — LangGraph Scientific State Specification

## Step

11.3 — LangGraph State Definition & Validation

## Purpose

Define the typed scientific orchestration state required by the approved
Step 11.2 LangGraph orchestration design.

This specification defines state only.

Graph compilation and graph execution are outside this step.

## Project

- Project: AI DDDD 360
- Version: 0.1.0
- Architecture: Disease-agnostic
- Current role-model validation: Parkinson's Disease
- Alzheimer validation: INACTIVE

## State Components

The state contains:

1. Project identity
2. Disease context
3. Scientific question
4. Evidence records
5. Interpretations
6. Inferences
7. Hypotheses
8. Uncertainties
9. Conflicting evidence
10. Unsupported assumptions
11. Biology Deficits
12. Agent outputs
13. Current agent
14. Execution trace
15. Human-review requirement
16. Execution status
17. Error messages
18. Parkinson role-model flag
19. Alzheimer validation flag

## Evidence Model

Evidence levels:

E0 — No evidence
E1 — Computational prediction
E2 — Molecular/biochemical evidence
E3 — Cellular evidence
E4 — Animal/preclinical evidence
E5 — Human observational evidence
E6 — Clinical trial evidence
E7 — Regulatory/validated clinical evidence

Safety invariant:

E1 must never be silently treated as equivalent to E6.

## Agent Output Contract

Each agent output preserves:

- agent identity
- agent version
- status
- evidence level
- structured output
- interpretation
- uncertainty
- Biology Deficits
- human-review requirement

## Biology Deficit Contract

Biology Deficits remain explicit.

A deficit may contain:

- identifier
- description
- evidence level
- uncertainty
- supporting evidence
- conflicting evidence
- resolution status

Unresolved deficits must not be silently converted into resolved conclusions.

## Execution Trace

Each execution trace record preserves:

- sequence
- node
- agent identity
- status
- timestamp

## Human Oversight

`human_review_required = True` remains part of the state contract.

The state does not authorize:

- therapeutic decisions
- clinical decisions
- autonomous wet-lab decisions

## Error Handling

Execution status is constrained to:

- INITIALIZED
- RUNNING
- PAUSED_FOR_HUMAN_REVIEW
- COMPLETED
- FAILED

Errors are explicitly stored in `error_messages`.

## Disease Boundary

Parkinson's Disease is the active role-model validation disease.

Alzheimer validation remains inactive.

The architecture remains disease-agnostic.

## Step 11.3 Execution Boundary

This step does NOT:

- compile a LangGraph
- execute a LangGraph
- invoke an LLM
- access external networks
- call external APIs
- make therapeutic recommendations
- make clinical recommendations
- make autonomous wet-lab decisions
- modify existing scientific agent implementations

## Deterministic Validation

Controlled state serialization is deterministic.

State SHA256:

74ce22f929150f0920744d398ccf678a2750cc168dc504eff8b3b68959063d0e

