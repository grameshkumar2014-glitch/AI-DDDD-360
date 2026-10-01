
"""
AI DDDD 360™ — Reusable Base Agent Foundation

Step 9.2F

Disease-agnostic foundation shared by all AI DDDD 360™ agents.

Scientific safety:
- Evidence and inference remain separate.
- Hypothesis and demonstrated effect remain separate.
- Conflicting evidence is preserved.
- Uncertainty is explicit.
- E1 is never silently treated as E6.
- Human oversight is required for consequential interpretation.
- No autonomous therapeutic, clinical, or wet-lab decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
import uuid


ALLOWED_EVIDENCE_LEVELS = (
    "E0", "E1", "E2", "E3",
    "E4", "E5", "E6", "E7"
)

BIOLOGY_DEFICIT_STATES = (
    "missing",
    "conflicting",
    "weak",
    "uncertain",
    "unsupported",
    "mechanistically_unresolved",
)


@dataclass
class EvidenceRecord:

    source_reference: str
    retrieval_provenance: str
    evidence_level: str
    temporal_context: str
    limitations: str
    uncertainty: str
    claim: str = ""

    def __post_init__(self):

        if self.evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            raise ValueError(
                f"Invalid evidence level: {self.evidence_level}"
            )

        if not self.source_reference:
            raise ValueError(
                "source_reference is required"
            )

        if not self.retrieval_provenance:
            raise ValueError(
                "retrieval_provenance is required"
            )


@dataclass
class BiologyDeficit:

    deficit_id: str
    description: str
    evidence: List[str]
    evidence_level: str
    uncertainty: str
    impact: str
    information_gap: str
    recommended_information_gain: str
    state: str

    def __post_init__(self):

        if self.state not in BIOLOGY_DEFICIT_STATES:
            raise ValueError(
                f"Invalid Biology Deficit state: {self.state}"
            )

        if self.evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            raise ValueError(
                f"Invalid evidence level: {self.evidence_level}"
            )


@dataclass
class ReproducibilityMetadata:

    project_version: str
    agent_version: str
    software_environment: str
    configuration: Dict[str, Any]
    data_evidence_provenance: str
    run_identifier: str
    model_version: str
    prompt_context_version: str
    random_seed: Optional[int]
    temporal_cutoff: Optional[str]
    evaluation_dataset: Optional[str]
    git_commit: str
    result: str
    interpretation: str
    limitations: List[str] = field(default_factory=list)


class BaseAgent:

    PLATFORM = "AI DDDD 360™"
    EVIDENCE_LEVELS = ALLOWED_EVIDENCE_LEVELS
    BIOLOGY_DEFICIT_STATES = BIOLOGY_DEFICIT_STATES

    def __init__(
        self,
        agent_id: str,
        agent_name: str,
        agent_version: str,
        purpose: str,
        scope: str,
        project_version: str = "0.1.0",
    ):

        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_version = agent_version
        self.purpose = purpose
        self.scope = scope
        self.project_version = project_version

    def create_run_identifier(self) -> str:

        return f"{self.agent_id}-{uuid.uuid4().hex[:12]}"

    def validate_input(
        self,
        payload: Dict[str, Any]
    ) -> None:

        required = [
            "agent_id",
            "agent_name",
            "agent_version",
            "run_identifier",
            "task",
            "context",
            "evidence",
            "ontology_context",
            "knowledge_graph_context",
            "reproducibility_metadata",
        ]

        missing = [
            key for key in required
            if key not in payload
        ]

        if missing:
            raise ValueError(
                f"Missing required input fields: {missing}"
            )

        if payload["agent_id"] != self.agent_id:
            raise ValueError(
                "Input agent_id does not match this agent"
            )

        if payload["agent_name"] != self.agent_name:
            raise ValueError(
                "Input agent_name does not match this agent"
            )

        if not isinstance(payload["evidence"], list):
            raise TypeError(
                "evidence must be a list"
            )

        if not isinstance(payload["ontology_context"], dict):
            raise TypeError(
                "ontology_context must be a dictionary"
            )

        if not isinstance(
            payload["knowledge_graph_context"],
            dict
        ):
            raise TypeError(
                "knowledge_graph_context must be a dictionary"
            )

    def validate_evidence(
        self,
        evidence: List[Dict[str, Any]]
    ) -> List[EvidenceRecord]:

        validated = []

        required = [
            "source_reference",
            "retrieval_provenance",
            "evidence_level",
            "temporal_context",
            "limitations",
            "uncertainty",
        ]

        for index, item in enumerate(evidence):

            missing = [
                key
                for key in required
                if key not in item
            ]

            if missing:
                raise ValueError(
                    f"Evidence record {index} missing: {missing}"
                )

            validated.append(
                EvidenceRecord(
                    source_reference=item[
                        "source_reference"
                    ],
                    retrieval_provenance=item[
                        "retrieval_provenance"
                    ],
                    evidence_level=item[
                        "evidence_level"
                    ],
                    temporal_context=item[
                        "temporal_context"
                    ],
                    limitations=item[
                        "limitations"
                    ],
                    uncertainty=item[
                        "uncertainty"
                    ],
                    claim=item.get("claim", ""),
                )
            )

        return validated

    def classify_evidence_strength(
        self,
        evidence: List[EvidenceRecord]
    ) -> Dict[str, Any]:

        counts = {
            level: 0
            for level in self.EVIDENCE_LEVELS
        }

        for record in evidence:
            counts[record.evidence_level] += 1

        return {
            "counts_by_level": counts,
            "evidence_levels_present": sorted(
                set(
                    r.evidence_level
                    for r in evidence
                )
            ),
            "e1_not_equivalent_to_e6": True,
        }

    def create_reasoning_record(
        self,
        evidence: List[str],
        interpretation: List[str],
        inference: List[str],
        hypotheses: List[str],
        demonstrated_effects: List[str],
        uncertainty: List[str],
        conflicting_evidence: List[str],
    ) -> Dict[str, Any]:

        return {
            "evidence": evidence,
            "interpretation": interpretation,
            "inference": inference,
            "hypothesis": hypotheses,
            "demonstrated_effect": demonstrated_effects,
            "uncertainty": uncertainty,
            "conflicting_evidence": conflicting_evidence,

            "evidence_vs_inference": {
                "evidence": evidence,
                "inference": inference,
            },

            "hypothesis_vs_demonstrated_effect": {
                "hypothesis": hypotheses,
                "demonstrated_effect": demonstrated_effects,
            },
        }

    def validate_biology_deficits(
        self,
        deficits: List[Dict[str, Any]]
    ) -> List[BiologyDeficit]:

        validated = []

        required = [
            "deficit_id",
            "description",
            "evidence",
            "evidence_level",
            "uncertainty",
            "impact",
            "information_gap",
            "recommended_information_gain",
            "state",
        ]

        for index, item in enumerate(deficits):

            missing = [
                key
                for key in required
                if key not in item
            ]

            if missing:
                raise ValueError(
                    f"Biology Deficit {index} missing: {missing}"
                )

            validated.append(
                BiologyDeficit(
                    deficit_id=item["deficit_id"],
                    description=item["description"],
                    evidence=item["evidence"],
                    evidence_level=item["evidence_level"],
                    uncertainty=item["uncertainty"],
                    impact=item["impact"],
                    information_gap=item[
                        "information_gap"
                    ],
                    recommended_information_gain=item[
                        "recommended_information_gain"
                    ],
                    state=item["state"],
                )
            )

        return validated

    def validate_reproducibility(
        self,
        metadata: Dict[str, Any]
    ) -> None:

        required = [
            "project_version",
            "agent_version",
            "software_environment",
            "configuration",
            "data_evidence_provenance",
            "run_identifier",
            "model_version",
            "prompt_context_version",
            "random_seed",
            "temporal_cutoff",
            "evaluation_dataset",
            "git_commit",
            "result",
            "interpretation",
            "limitations",
        ]

        missing = [
            key
            for key in required
            if key not in metadata
        ]

        if missing:
            raise ValueError(
                f"Missing reproducibility fields: {missing}"
            )

    def human_oversight_record(
        self,
        required: bool = True,
        reviewed: bool = False,
        reviewer: Optional[str] = None,
    ) -> Dict[str, Any]:

        return {
            "required": required,
            "reviewed": reviewed,
            "reviewer": reviewer,
            "autonomous_therapeutic_decision": False,
            "autonomous_clinical_recommendation": False,
            "autonomous_wet_lab_decision": False,
        }

    def build_output(
        self,
        payload: Dict[str, Any],
        findings: List[str],
        reasoning: Dict[str, Any],
        biology_deficits: List[BiologyDeficit],
        evidence: List[EvidenceRecord],
        reproducibility_metadata: Dict[str, Any],
        human_oversight: Dict[str, Any],
        limitations: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        self.validate_input(payload)

        self.validate_reproducibility(
            reproducibility_metadata
        )

        evidence_summary = (
            self.classify_evidence_strength(
                evidence
            )
        )

        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "agent_version": self.agent_version,
            "run_identifier": payload[
                "run_identifier"
            ],
            "task": payload["task"],
            "findings": findings,

            "supporting_evidence": [
                asdict(e)
                for e in evidence
            ],

            "conflicting_evidence": reasoning[
                "conflicting_evidence"
            ],

            "evidence_vs_inference": reasoning[
                "evidence_vs_inference"
            ],

            "hypothesis_vs_demonstrated_effect": reasoning[
                "hypothesis_vs_demonstrated_effect"
            ],

            "uncertainty": reasoning[
                "uncertainty"
            ],

            "limitations": limitations or [],

            "biology_deficits": [
                asdict(d)
                for d in biology_deficits
            ],

            "provenance": [
                {
                    "source_reference":
                        e.source_reference,
                    "retrieval_provenance":
                        e.retrieval_provenance,
                    "temporal_context":
                        e.temporal_context,
                }
                for e in evidence
            ],

            "evidence_summary": evidence_summary,

            "human_oversight": human_oversight,

            "reproducibility_metadata":
                reproducibility_metadata,

            "scientific_safety": {
                "evidence_inference_separated": True,
                "hypothesis_demonstrated_effect_separated": True,
                "conflicting_evidence_preserved": True,
                "uncertainty_explicit": True,
                "e1_not_equivalent_to_e6": True,
                "autonomous_therapeutic_decision": False,
                "autonomous_clinical_recommendation": False,
                "autonomous_wet_lab_decision": False,
            },
        }

    def run_foundation(
        self,
        payload: Dict[str, Any],
        findings: Optional[List[str]] = None,
        reasoning: Optional[Dict[str, Any]] = None,
        biology_deficits: Optional[
            List[Dict[str, Any]]
        ] = None,
    ) -> Dict[str, Any]:

        self.validate_input(payload)

        evidence = self.validate_evidence(
            payload["evidence"]
        )

        deficits = self.validate_biology_deficits(
            biology_deficits or []
        )

        if reasoning is None:
            reasoning = self.create_reasoning_record(
                evidence=[],
                interpretation=[],
                inference=[],
                hypotheses=[],
                demonstrated_effects=[],
                uncertainty=[],
                conflicting_evidence=[],
            )

        self.validate_reproducibility(
            payload["reproducibility_metadata"]
        )

        return self.build_output(
            payload=payload,
            findings=findings or [],
            reasoning=reasoning,
            biology_deficits=deficits,
            evidence=evidence,
            reproducibility_metadata=payload[
                "reproducibility_metadata"
            ],
            human_oversight=self.human_oversight_record(),
        )


__all__ = [
    "BaseAgent",
    "EvidenceRecord",
    "BiologyDeficit",
    "ReproducibilityMetadata",
    "ALLOWED_EVIDENCE_LEVELS",
    "BIOLOGY_DEFICIT_STATES",
]
