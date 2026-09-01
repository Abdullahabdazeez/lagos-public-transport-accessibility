from __future__ import annotations

import csv
import math
from pathlib import Path

import geopandas as gpd


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CITATION.cff",
    "LICENSE",
    "project.json",
    "data/final/Lagos_LGA_Formal_Transit_Accessibility_FINAL.gpkg",
    "data/tables/key_findings.csv",
    "data/tables/project_statistics.csv",
    "data/tables/public_interpretation.txt",
    "docs/DATA_SOURCES.md",
    "docs/FINAL_TECHNICAL_REPORT.md",
    "docs/LIMITATIONS.md",
    "docs/METHODOLOGY.md",
    "docs/PORTFOLIO_PROJECT_SUMMARY.md",
    "docs/RESULTS.md",
    "reports/Lagos_Final_Technical_Report.pdf",
]

EXPECTED = {
    "Analysis population": (11_613_844.0, 100.0),
    "Within 15 minutes of mapped formal/core transit": (2_557_743.350246872, 22.023228056506287),
    "Within 30 minutes of mapped formal/core transit": (6_206_326.219712599, 53.439035514103686),
    "Within 45 minutes of mapped formal/core transit": (8_350_755.804961861, 71.90346111900472),
    "Within 60 minutes of mapped formal/core transit": (9_232_087.717288893, 79.49209337828968),
    "Beyond 30 minutes or structural formal-network gap": (5_407_517.780287401, 46.56096448589633),
}


def require_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise AssertionError("Missing required files:\n- " + "\n- ".join(missing))


def read_statistics() -> dict[str, tuple[float, float | None]]:
    path = ROOT / "data/tables/project_statistics.csv"
    rows: dict[str, tuple[float, float | None]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            percent = float(row["Percent"]) if row["Percent"].strip() else None
            rows[row["Metric"]] = (float(row["Value"]), percent)
    return rows


def validate_statistics(rows: dict[str, tuple[float, float | None]]) -> None:
    for metric, (expected_value, expected_percent) in EXPECTED.items():
        if metric not in rows:
            raise AssertionError(f"Missing authoritative metric: {metric}")
        value, percent = rows[metric]
        if not math.isclose(value, expected_value, rel_tol=0, abs_tol=1e-6):
            raise AssertionError(f"Unexpected value for {metric}: {value}")
        if expected_percent is not None:
            if percent is None or not math.isclose(percent, expected_percent, rel_tol=0, abs_tol=1e-9):
                raise AssertionError(f"Unexpected percentage for {metric}: {percent}")

    population = rows["Analysis population"][0]
    within_30 = rows["Within 30 minutes of mapped formal/core transit"][0]
    gap_30 = rows["Beyond 30 minutes or structural formal-network gap"][0]
    if not math.isclose(within_30 + gap_30, population, rel_tol=0, abs_tol=1e-5):
        raise AssertionError("30-minute access and gap populations do not sum to the analysis population.")

    access_pct = rows["Within 30 minutes of mapped formal/core transit"][1]
    gap_pct = rows["Beyond 30 minutes or structural formal-network gap"][1]
    if access_pct is None or gap_pct is None or not math.isclose(access_pct + gap_pct, 100.0, abs_tol=1e-9):
        raise AssertionError("30-minute access and gap percentages do not sum to 100%.")


def validate_geopackage() -> None:
    path = ROOT / "data/final/Lagos_LGA_Formal_Transit_Accessibility_FINAL.gpkg"
    frame = gpd.read_file(path)
    if frame.empty:
        raise AssertionError("Final GeoPackage contains no features.")
    if frame.crs is None:
        raise AssertionError("Final GeoPackage has no CRS.")
    if not frame.geometry.notna().all():
        raise AssertionError("Final GeoPackage contains missing geometries.")


def validate_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrases = [
        "formal/core public-transport",
        "53.44%",
        "46.56%",
        "219",
        "informal/paratransit",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in readme]
    if missing:
        raise AssertionError("README is missing required interpretation text: " + ", ".join(missing))


def main() -> None:
    require_files()
    statistics = read_statistics()
    validate_statistics(statistics)
    validate_geopackage()
    validate_readme()
    print("Repository validation passed.")
    print(f"Required files checked: {len(REQUIRED_FILES)}")
    print("Authoritative statistics: consistent")
    print("Final GeoPackage: readable, non-empty, CRS present")
    print("README interpretation safeguards: present")


if __name__ == "__main__":
    main()
