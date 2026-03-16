import tomllib
from pathlib import Path


def test_pyproject_can_install_project_scripts() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["scripts"]
    assert "build-system" in pyproject or pyproject.get("tool", {}).get("uv", {}).get("package") is True
