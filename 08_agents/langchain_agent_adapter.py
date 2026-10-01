from pydantic import BaseModel, Field
from langchain_core.runnables import Runnable, RunnableLambda

class ScientificAgentInput(BaseModel):
    project_id: str = "AI-DDDD-360"
    disease_context: str = "Parkinson's disease"
    biological_question: str
    evidence_records: list = Field(default_factory=list)
    ontology_context: dict = Field(default_factory=dict)
    knowledge_graph_context: dict = Field(default_factory=dict)
    rag_context: list = Field(default_factory=list)
    uncertainty: list = Field(default_factory=list)
    temporal_cutoff: str | None = None
    execution_id: str = "STEP_10_4_CONTROLLED_E0"

class ScientificAgentOutput(BaseModel):
    agent_identity: str
    question_addressed: str
    evidence_used: list = Field(default_factory=list)
    evidence_level: list = Field(default_factory=list)
    interpretation: list = Field(default_factory=list)
    inference: list = Field(default_factory=list)
    hypothesis: list = Field(default_factory=list)
    demonstrated_effect_status: list = Field(default_factory=list)
    conflicting_evidence: list = Field(default_factory=list)
    uncertainty: list = Field(default_factory=list)
    unsupported_assumptions: list = Field(default_factory=list)
    biology_deficit: list = Field(default_factory=list)
    provenance: list = Field(default_factory=list)
    limitations: list = Field(default_factory=list)
    reproducibility_metadata: dict = Field(default_factory=dict)
    human_review_required: bool = True

class LangChainScientificAgentAdapter:
    def __init__(self, agent):
        self.agent = agent
        self.agent_identity = getattr(
            agent, "name", agent.__class__.__name__
        )

    def invoke(self, input_data):
        request = (
            ScientificAgentInput(**input_data)
            if isinstance(input_data, dict)
            else input_data
        )

        output = ScientificAgentOutput(
            agent_identity=self.agent_identity,
            question_addressed=request.biological_question,
            evidence_used=request.evidence_records,
            evidence_level=["E0"],
            uncertainty=request.uncertainty,
            limitations=[
                "Controlled E0 LangChain integration boundary.",
                "Substantive biological reasoning not executed.",
                "LLM execution not activated.",
                "External network execution not activated.",
            ],
            reproducibility_metadata={
                "project_id": request.project_id,
                "execution_id": request.execution_id,
                "disease_context": request.disease_context,
                "temporal_cutoff": request.temporal_cutoff,
                "integration_step": "10.4",
            },
            human_review_required=True,
        )

        return output.model_dump()
