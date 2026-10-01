# AI DDDD 360™
# Core Agent Scientific Execution Specification

## Status

Controlled specification for Step 9.3.

This specification defines the scientific execution boundary for the
eight core agents using the already validated AI DDDD 360™ foundation.

It does not introduce LangChain, LangGraph, LangSmith, external LLM
execution, autonomous therapeutic decision-making, autonomous wet-lab
execution, or clinical recommendations.

## Platform Principle

BEFORE YOU INVEST IN THE NEXT EXPERIMENT, KNOW WHAT YOU DON'T KNOW.

## 1. Scientific Execution Contract

Every core agent execution must preserve:

1. Evidence as distinct from interpretation.
2. Interpretation as distinct from inference.
3. Hypothesis as distinct from demonstrated effect.
4. Supporting evidence.
5. Conflicting evidence.
6. Explicit uncertainty.
7. Unsupported assumptions.
8. Evidence provenance.
9. Temporal context.
10. Evidence level E0–E7.
11. Biology Deficits where applicable.
12. Human oversight.
13. Reproducibility metadata.

The system must never silently treat E1 evidence as equivalent to E6
evidence.

## 2. Evidence Handling

Agent execution must preserve the established evidence hierarchy:

E0 — No evidence  
E1 — Computational prediction  
E2 — Molecular / biochemical evidence  
E3 — Cellular evidence  
E4 — Animal / preclinical evidence  
E5 — Human observational evidence  
E6 — Clinical trial evidence  
E7 — Regulatory / validated clinical evidence

Agents must not silently upgrade, downgrade, merge, or reinterpret
evidence levels.

## 3. Conflict and Uncertainty

An agent must preserve conflicting evidence rather than silently
selecting one interpretation.

Uncertainty must remain explicit.

When evidence is absent, weak, conflicting, uncertain, unsupported,
or mechanistically unresolved, the relevant Biology Deficit must be
represented.

## 4. BBE-BD

Where applicable, agent reasoning must preserve the distinction:

Bimodality → Binding → Efficacy → Biology Deficit

Binding must not be treated as equivalent to efficacy.

The efficacy chain remains:

Target engagement →
Pathway modulation →
Cellular response →
Disease phenotype →
Therapeutic effect

## 5. RAG Compatibility

Agent execution must accept and preserve the established RAG
provenance model, including source reference, retrieval provenance,
evidence level, temporal context, limitations, and uncertainty.

## 6. Ontology Compatibility

Agent entities and relationships must remain compatible with the
validated AI DDDD 360™ ontology and ontology registry.

## 7. Knowledge Graph Compatibility

Agent outputs must remain representable through the established
knowledge-graph foundation without silently introducing unsupported
entity or relationship types.

## 8. Biology Deficit Interface

Every core agent must be capable of identifying relevant Biology
Deficits.

Biology Deficit states:

- missing
- conflicting
- weak
- uncertain
- unsupported
- mechanistically unresolved

## 9. Human Oversight

Human oversight remains mandatory for:

- therapeutic interpretation
- candidate prioritization
- clinical interpretation
- experimental decisions
- safety conclusions
- patient stratification

No agent is authorized to make autonomous therapeutic or clinical
decisions.

## 10. Reproducibility

Every future substantive agent execution must preserve:

- project version
- agent version
- software environment
- configuration
- data/evidence provenance
- run identifier
- model version
- prompt/context version
- random seed where applicable
- temporal cutoff
- evaluation dataset
- Git commit
- result
- interpretation
- limitations

## 11. Core Agents


### 1. Disease Biology Agent

- Agent ID: AG-DIS-001
- Purpose: Analyze disease biology, mechanisms, disease states, disease-stage context, and biological evidence relevant to drug discovery and development.
- Scope: ['disease mechanisms', 'disease biology', 'disease states', 'disease stage', 'pathways', 'cellular context', 'human biological evidence']
- Primary inputs: ['disease entities', 'genes', 'proteins', 'pathways', 'multi-omics evidence', 'human evidence', 'retrieved evidence']
- Required evidence: ['evidence level', 'source reference', 'temporal context', 'supporting evidence', 'conflicting evidence']
- Primary outputs: ['disease biology findings', 'mechanistic interpretations', 'evidence conflicts', 'uncertainty', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 2. Target Intelligence Agent

- Agent ID: AG-TGT-001
- Purpose: Evaluate target-related biological evidence, target validity, human relevance, mechanistic support, and unresolved target uncertainties.
- Scope: ['target validity', 'target biology', 'human genetics', 'human evidence', 'druggability', 'mechanistic support']
- Primary inputs: ['targets', 'genes', 'proteins', 'disease biology', 'human evidence', 'multi-omics evidence']
- Required evidence: ['target evidence', 'human evidence', 'evidence level', 'supporting evidence', 'conflicting evidence']
- Primary outputs: ['target intelligence', 'target evidence assessment', 'uncertainty', 'Biology Deficits', 'information needs']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 3. Multi-Omics & Bimodality Agent

- Agent ID: AG-OMX-001
- Purpose: Integrate multi-omics evidence and characterize bimodality across biological context, cell type, tissue, disease stage, patient subgroup, and molecular state.
- Scope: ['genomics', 'transcriptomics', 'proteomics', 'metabolomics', 'epigenomics', 'single-cell biology', 'spatial biology', 'bimodality']
- Primary inputs: ['multi-omics datasets', 'omics observations', 'cell types', 'tissues', 'disease stages', 'patient subgroups', 'molecular states']
- Required evidence: ['data provenance', 'evidence level', 'temporal context', 'biological context', 'uncertainty']
- Primary outputs: ['multi-omics findings', 'bimodality characterization', 'subgroup signals', 'uncertainty', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 4. Structure & Binding Agent

- Agent ID: AG-STB-001
- Purpose: Analyze molecular structure, target interaction, binding evidence, target engagement, and limitations while explicitly separating binding from efficacy.
- Scope: ['molecular structure', 'binding', 'target interaction', 'target engagement', 'structure-based evidence']
- Primary inputs: ['targets', 'proteins', 'molecular structures', 'binding evidence', 'computational predictions', 'biochemical evidence']
- Required evidence: ['binding evidence', 'evidence level', 'source provenance', 'model limitations', 'uncertainty']
- Primary outputs: ['binding findings', 'target engagement interpretation', 'binding uncertainty', 'conflicting evidence', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 5. Efficacy & Translational Agent

- Agent ID: AG-EFF-001
- Purpose: Analyze the progression from target engagement through pathway modulation, cellular response, disease phenotype, and therapeutic effect, while assessing translational uncertainty.
- Scope: ['target engagement', 'pathway modulation', 'cellular response', 'disease phenotype', 'therapeutic effect', 'translation']
- Primary inputs: ['binding evidence', 'target engagement', 'pathway evidence', 'cellular evidence', 'animal evidence', 'human evidence']
- Required evidence: ['efficacy evidence', 'evidence level', 'translational evidence', 'conflicting evidence', 'uncertainty']
- Primary outputs: ['efficacy findings', 'translational assessment', 'evidence conflicts', 'uncertainty', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 6. ADMET & Safety Agent

- Agent ID: AG-ADS-001
- Purpose: Analyze absorption, distribution, metabolism, excretion, toxicity, safety evidence, liabilities, and unresolved safety uncertainties.
- Scope: ['ADME', 'pharmacokinetics', 'toxicity', 'safety', 'off-target liabilities', 'preclinical safety']
- Primary inputs: ['drug candidates', 'molecular structures', 'ADMET evidence', 'toxicity evidence', 'preclinical evidence', 'clinical safety evidence']
- Required evidence: ['safety evidence', 'evidence level', 'source provenance', 'limitations', 'uncertainty']
- Primary outputs: ['ADMET findings', 'safety findings', 'safety liabilities', 'uncertainty', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 7. Clinical Intelligence Agent

- Agent ID: AG-CIN-001
- Purpose: Analyze clinical development evidence, clinical trial findings, failure signals, biomarkers, patient stratification, disease stage, and translational lessons.
- Scope: ['clinical trials', 'clinical evidence', 'trial outcomes', 'biomarkers', 'patient stratification', 'disease stage', 'clinical translation']
- Primary inputs: ['clinical trials', 'clinical evidence', 'drug candidates', 'biomarkers', 'patient subgroups', 'disease stages']
- Required evidence: ['clinical evidence', 'trial provenance', 'evidence level', 'temporal context', 'conflicting evidence']
- Primary outputs: ['clinical intelligence', 'trial lessons', 'translational risks', 'uncertainty', 'Biology Deficits']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}

### 8. Biology Deficit Agent

- Agent ID: AG-BD-001
- Purpose: Identify, characterize, prioritize, and resolve unresolved biological knowledge deficits that could contribute to drug discovery or development failure.
- Scope: ['missing evidence', 'conflicting evidence', 'weak evidence', 'uncertain evidence', 'unsupported claims', 'mechanistically unresolved biology', 'information gain']
- Primary inputs: ['outputs from core agents', 'evidence conflicts', 'uncertainty', 'ontology entities', 'knowledge graph relationships', 'RAG evidence']
- Required evidence: ['evidence level', 'supporting evidence', 'conflicting evidence', 'uncertainty', 'provenance']
- Primary outputs: ['Biology Deficits', 'deficit classification', 'information needs', 'highest-information next steps', 'experimental information requirements']
- Biology Deficit interface: {'enabled': True, 'required_when': ['evidence is missing', 'evidence conflicts', 'evidence is weak', 'evidence is uncertain', 'claim is unsupported', 'mechanism remains unresolved']}


## 12. Implementation Boundary

Step 9.3 establishes the scientific execution contract only.

The following remain outside this step:

- LangChain implementation
- LangGraph orchestration
- LangSmith evaluation
- autonomous LLM execution
- external network execution
- autonomous therapeutic decisions
- autonomous clinical recommendations
- autonomous wet-lab decisions
- final clinical candidate ranking

## 13. Validation Role

Parkinson's Disease remains the AI DDDD 360™ role-model validation
case.

The architecture remains disease-agnostic.

The Alzheimer validation track is not used for AI DDDD 360™.

## 14. Change Control

No major architectural change may be introduced silently.

Any future change must record:

- date
- change
- reason
