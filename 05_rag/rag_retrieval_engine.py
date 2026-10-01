from pathlib import Path
import json
import hashlib


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_retrieval_record(record_path):
    path = Path(record_path)
    if not path.exists():
        raise FileNotFoundError(f"Retrieval record not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate_retrieval_record(record):
    required = [
        "record_type",
        "project",
        "project_version",
        "evidence_level",
        "source_reference",
        "source_identifier",
        "temporal_cutoff",
        "retrieval_query",
        "retrieved_content_reference",
        "interpretation",
        "limitations",
        "supporting_evidence",
        "conflicting_evidence",
        "uncertainty",
        "evidence_vs_inference",
        "hypothesis_vs_demonstrated_effect",
        "human_oversight_required",
        "experiment_id",
        "model_version",
        "prompt_version",
        "context_version",
        "random_seed",
        "evaluation_dataset",
        "git_commit",
        "source_sha256",
        "retrieval_timestamp_utc",
        "results_reference",
    ]

    missing = [field for field in required if field not in record]

    if missing:
        raise ValueError(
            "Retrieval record missing required fields: "
            + ", ".join(missing)
        )

    if record["evidence_level"] not in {
        "E0", "E1", "E2", "E3",
        "E4", "E5", "E6", "E7"
    }:
        raise ValueError("Invalid evidence level.")

    if record["computational_prediction_is_clinical_evidence"] is not False:
        raise ValueError(
            "Computational prediction cannot be treated as clinical evidence."
        )

    if record["therapeutic_conclusion_from_retrieval_alone"] is not False:
        raise ValueError(
            "Retrieval alone cannot establish a therapeutic conclusion."
        )

    if record["human_oversight_required"] is not True:
        raise ValueError(
            "Human oversight must remain required."
        )

    return True


def retrieve_records(records, query):
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Retrieval query must be a non-empty string.")

    query_terms = {
        term.lower()
        for term in query.split()
        if term.strip()
    }

    results = []

    for record in records:
        validate_retrieval_record(record)

        searchable = " ".join([
            str(record.get("retrieval_query", "")),
            str(record.get("interpretation", "")),
            str(record.get("limitations", "")),
            str(record.get("uncertainty", "")),
            str(record.get("source_reference", "")),
        ]).lower()

        matches = sum(
            1 for term in query_terms
            if term in searchable
        )

        if matches > 0:
            result = dict(record)
            result["retrieval_match_count"] = matches
            results.append(result)

    results.sort(
        key=lambda item: item["retrieval_match_count"],
        reverse=True
    )

    return results
