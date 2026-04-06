from datetime import datetime


def validate_result(results):
    """Validate result completeness and provide diagnostics."""
    summary = results.get("summary", "")
    has_summary = isinstance(summary, str) and bool(summary.strip())

    return {
        "is_valid": bool(results.get("ok")) and has_summary,
        "has_summary": has_summary,
        "trace_steps": len(results.get("trace", [])),
        "validated_at": datetime.utcnow().isoformat() + "Z",
    }
