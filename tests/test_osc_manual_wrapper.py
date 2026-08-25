from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_setup_uv_explicitly_disables_target_influenced_cache():
    """The arbitrary-ref runner must never restore or save target-controlled caches."""
    workflow = yaml.safe_load(
        (ROOT / ".github/workflows/osc-manual.yml").read_text(encoding="utf-8")
    )
    setup_uv_steps = [
        step
        for step in workflow["jobs"]["test"]["steps"]
        if step.get("uses", "").startswith("astral-sh/setup-uv@")
    ]

    assert len(setup_uv_steps) == 1
    assert setup_uv_steps[0].get("with", {}).get("enable-cache") is False
