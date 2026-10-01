# AI DDDD 360 — LangGraph Node Adapter Specification

## Step

11.4 — LangGraph Node Adapter Design & Validation

## Validation Correction

The initial Step 11.4 validator supplied `scientific_question` to the
validated LangChain adapter.

The actual validated `ScientificAgentInput` contract requires:

`biological_question`

The adapter implementation was NOT modified.

The validation fixture was corrected to match the actual existing contract.

## Approved Architecture

Scientific Agent
    ->
LangChainScientificAgentAdapter.invoke()
    ->
RunnableLambda
    ->
LangGraph Node
    ->
ScientificOrchestrationState

## Existing Validated Adapter

SHA256:

`f6b30812b80909b60048237e7de7ddf2a9f772ea9731f331fe58e9a586d32c74`

## Eight Scientific Nodes

1. Disease Biology Agent
2. Target Intelligence Agent
3. Multi-Omics & Bimodality Agent
4. Structure & Binding Agent
5. Efficacy & Translational Agent
6. ADMET & Safety Agent
7. Clinical Intelligence Agent
8. Biology Deficit Agent

## Node Contract

Each node:

- receives structured state
- maps state to the actual adapter input contract
- uses `biological_question`
- invokes the validated LangChain adapter
- receives structured output
- appends agent output
- appends execution trace
- preserves E0 in the controlled fixture
- preserves human review
- preserves Parkinson role-model validation
- keeps Alzheimer validation inactive

## Safety Boundary

No:

- LLM execution
- external network access
- external API access
- graph compilation
- graph execution
- therapeutic recommendation
- clinical recommendation
- autonomous wet-lab decision
- substantive biological reasoning

## Implementation Boundary

Existing scientific agents and the validated LangChain adapter are unchanged.

## Disease Boundary

Parkinson's Disease = active role-model.

Alzheimer validation = inactive.

