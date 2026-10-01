"""
AI DDDD 360™ — Controlled Data Ingestion

Step 5 — Data ingestion.

This module provides a minimal, provenance-preserving local ingestion
mechanism. It does not define an external source, API, database, schema,
or ingestion schedule because those implementation details are not specified
by the Master Control.

The module is intentionally limited to preserving supplied source content
and its reproducibility/provenance context.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256_file(path: str | Path) -> str:
    """Return the SHA256 hash of a file."""
    file_path = Path(path)

    digest = hashlib.sha256()

    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def ingest_local_file(
    source_path: str | Path,
    destination_dir: str | Path,
    *,
    evidence_level: str,
    source_reference: str,
    temporal_cutoff: str,
    interpretation: str | None = None,
    limitations: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Ingest a supplied local file while preserving provenance metadata.

    The caller must explicitly provide the evidence level and provenance
    information. The function does not infer scientific evidence level,
    efficacy, clinical significance, or therapeutic conclusions.
    """

    source = Path(source_path)
    destination = Path(destination_dir)

    if not source.is_file():
        raise FileNotFoundError(f"Source file not found: {source}")

    destination.mkdir(parents=True, exist_ok=True)

    output_file = destination / source.name
    output_file.write_bytes(source.read_bytes())

    source_hash = sha256_file(source)
    ingested_hash = sha256_file(output_file)

    if source_hash != ingested_hash:
        raise ValueError(
            "Integrity validation failed: source and ingested file hashes differ."
        )

    captured_utc = datetime.now(timezone.utc).isoformat()

    record = {
        "source_file": str(source),
        "ingested_file": str(output_file),
        "source_reference": source_reference,
        "evidence_level": evidence_level,
        "temporal_cutoff": temporal_cutoff,
        "source_sha256": source_hash,
        "ingested_sha256": ingested_hash,
        "captured_utc": captured_utc,
        "interpretation": interpretation,
        "limitations": limitations,
        "metadata": metadata or {},
    }

    return record


def save_ingestion_record(
    record: dict[str, Any],
    record_path: str | Path,
) -> Path:
    """Save an ingestion provenance record as JSON."""

    output = Path(record_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        json.dumps(record, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return output
