# AI DDDD 360™ — Core Agent Foundation Specification

## 1. Purpose

The Core Agent Foundation defines the common scientific, evidence,
provenance, uncertainty, safety, and reproducibility contract for the
AI DDDD 360™ core agents.

The foundation does not itself make therapeutic or clinical decisions.
Agents operate as evidence-grounded intelligence components under
human oversight.

## 2. Platform Principle

BEFORE YOU INVEST IN THE NEXT EXPERIMENT, KNOW WHAT YOU DON'T KNOW.

The agents must distinguish established evidence, computational
inference, hypothesis, uncertainty, conflicting evidence, and
unresolved Biology Deficits.

## 3. Core Agents

The initial core agents are:

1. Disease Biology Agent
2. Target Intelligence Agent
3. Multi-Omics & Bimodality Agent
4. Structure & Binding Agent
5. Efficacy & Translational Agent
6. ADMET & Safety Agent
7. Clinical Intelligence Agent
8. Biology Deficit Agent

## 4. Common Agent Contract

Every core agent must define:

- agent_id
- agent_name
- agent_version
- purpose
- scope
- inputs
- required evidence
- evidence provenance
- processing / reasoning function
- outputs
- evidence levels
- supporting evidence
- conflicting evidence
- evidence_vs_inference
- hypothesis_vs_demonstrated_effect
- uncertainty
- limitations
- Biology Deficits where applicable
- reproducibility metadata
- human oversight requirements

## 5. Evidence Contract

Agents must preserve the AI DDDD 360™ evidence hierarchy:

- E0 — No evidence
- E1 — Computational prediction
- E2 — Molecular / biochemical evidence
- E3 — Cellular evidence
- E4 — Animal / preclinical evidence
- E5 — Human observational evidence
- E6 — Clinical trial evidence
- E7 — Regulatory / validated clinical evidence

The system must never silently treat E1 evidence as equivalent to E6
evidence.

Evidence level must remain attached to the relevant conclusion,
claim, or inference.

## 6. Evidence and Inference Separation

Every agent must distinguish:

1. Evidence directly supported by source material.
2. Interpretation derived from evidence.
3. Computational inference.
4. Hypothesis.
5. Demonstrated effect.

Agents must not convert an inference or hypothesis into demonstrated
effect without appropriate evidence.

## 7. Conflicting Evidence

Agents must explicitly preserve conflicting evidence.

Where evidence conflicts, the agent must:

- identify the conflicting findings;
- preserve provenance;
- identify evidence levels;
- describe the uncertainty;
- avoid silently selecting one conclusion;
- identify what additional evidence could resolve the conflict.

## 8. Uncertainty

Every agent must identify relevant uncertainty.

Uncertainty may arise from:

- insufficient evidence;
- conflicting evidence;
- limited biological context;
- disease-stage differences;
- patient-subgroup differences;
- model limitations;
- incomplete multi-omics evidence;
- unresolved mechanism;
- limited translational evidence;
- incomplete safety information.

## 9. Biology Deficit

Where the available evidence does not adequately support a biological
conclusion, the agent must identify the unresolved Biology Deficit.

The Biology Deficit may be:

- missing;
- conflicting;
- weak;
- uncertain;
- unsupported;
- mechanistically unresolved.

The Biology Deficit Agent provides dedicated analysis of these gaps.

## 10. BBE-BD Framework

The foundation preserves:

Bimodality → Binding → Efficacy → Biology Deficit

Binding must not be interpreted as efficacy.

The efficacy chain is:

Target engagement →
Pathway modulation →
Cellular response →
Disease phenotype →
Therapeutic effect

## 11. RAG and Evidence Provenance

Where retrieval is used, the agent must preserve:

- source reference;
- retrieval provenance;
- evidence level;
- temporal context;
- interpretation;
- limitations;
- uncertainty.

Retrieved material must not automatically be treated as validated
clinical evidence.

## 12. Ontology and Knowledge Graph Compatibility

Agent inputs and outputs must remain compatible with the validated
AI DDDD 360™ ontology and knowledge graph foundation.

The validated AI DDDD 360™ ontology is authoritative for agent
entity and relationship terminology.

Agent entities and relationships must use the established ontology
registry rather than silently introducing uncontrolled terminology.

The ontology registry must be treated as the controlled source for
the established entity and relationship definitions.

## 13. Human Oversight

Agents are decision-support intelligence components.

Human review is required where outputs could affect:

- therapeutic interpretation;
- candidate prioritization;
- clinical interpretation;
- experimental decisions;
- safety conclusions;
- patient stratification.

Agents must not present computational predictions as clinical evidence.

## 14. Reproducibility

Each agent execution must support reproducibility metadata including,
where applicable:

- project version;
- agent version;
- software environment;
- configuration;
- data/evidence provenance;
- experiment or run identifier;
- model version;
- prompt/context version;
- random seed;
- temporal cutoff;
- evaluation dataset;
- Git commit;
- result;
- interpretation;
- limitations.

## 15. Common Input Categories

Agent inputs may include:

- disease biology;
- targets;
- genes;
- proteins;
- pathways;
- multi-omics observations;
- bimodality features;
- molecular structures;
- binding evidence;
- efficacy evidence;
- ADMET and safety evidence;
- biomarkers;
- patient stratification;
- disease stage;
- clinical trial evidence;
- drug candidates;
- repurposing candidates;
- Biology Deficits;
- retrieved evidence;
- knowledge graph entities and relationships.

## 16. Common Output Categories

Agent outputs may include:

- evidence-grounded findings;
- evidence summaries;
- evidence conflicts;
- uncertainty statements;
- mechanistic interpretations;
- hypotheses;
- Biology Deficits;
- candidate intelligence;
- experimental information needs;
- recommended information-gathering priorities.

Outputs must preserve provenance and evidence level.

## 17. Scientific Safety

The foundation must preserve:

- human oversight;
- evidence versus inference;
- hypothesis versus demonstrated effect;
- uncertainty;
- conflicting evidence;
- provenance;
- limitations;
- appropriate validation before therapeutic conclusions.

## 18. Disease-Agnostic Architecture

The platform architecture remains disease-agnostic.

Parkinson’s Disease is the role-model validation case for AI DDDD 360™.
This validation role does not make the core agent architecture
Parkinson-specific.

## 19. Non-Goals for Foundation Stage

This foundation specification does not implement:

- autonomous therapeutic decision making;
- clinical recommendations;
- production deployment;
- external clinical claims;
- autonomous wet-lab execution;
- final candidate ranking;
- LangChain orchestration;
- LangGraph orchestration;
- LangSmith evaluation.

Those capabilities require subsequent controlled implementation
steps and validation.

## 20. Completion Criteria

The Core Agent Foundation is considered specified when:

1. All eight core agents are defined.
2. The common agent contract is defined.
3. Evidence hierarchy E0–E7 is preserved.
4. Evidence and inference are separated.
5. Conflicting evidence is preserved.
6. Uncertainty is preserved.
7. Biology Deficit handling is defined.
8. BBE-BD is preserved.
9. RAG provenance requirements are defined.
10. Ontology compatibility is defined.
11. Human oversight is defined.
12. Reproducibility requirements are defined.
13. Disease-agnostic architecture is preserved.
14. Parkinson’s role-model validation is preserved.
15. Non-goals prevent premature implementation.
