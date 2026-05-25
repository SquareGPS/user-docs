"""
rename_expert_center_assets.py

Renames Expert Center .gitbook/assets files that have generic or cryptic
WordPress/Confluence-generated names to descriptive slugs, and updates
all markdown references in docs/expert-center/.

Usage:
    python scripts/rename_expert_center_assets.py --dry-run   # preview only
    python scripts/rename_expert_center_assets.py             # apply
"""

import re
import argparse
from pathlib import Path

EC_ROOT = Path("docs/expert-center")
ASSETS  = EC_ROOT / ".gitbook" / "assets"

# ── Rename mapping  (old_basename → new_basename) ─────────────────────────────
# Only assets we added in the recovery commit are listed here.
# Alt text / section source is noted in the comment for each entry.

RENAMES = {
    # CAN article — "CAN bus: some principles behind" section
    "1.jpg":    "can-bus-principles-1.jpg",       # CAN and alternatives, 442x234
    "2-1.png":  "can-bus-principles-2.png",       # CAN and alternatives, 444x386
    "3-1.png":  "can-bus-principles-3.png",       # CAN and alternatives, 468x193
    "4.png":    "can-bus-principles-4.png",       # CAN and alternatives, 414x317
    "5.png":    "can-bus-principles-5.png",       # CAN and alternatives, 380x267
    # CAN article — "Wireless CAN" section
    "1-1.png":  "wireless-can-diagram.png",       # CAN and alternatives, 374x161
    # CAN article — "MOST, FlexRay and Automotive Ethernet in brief" section
    "3-2.png":  "most-flexray-diagram.png",       # CAN and alternatives, 474x102

    # Fuel level sensors — README (Liquid level sensing / overview)
    "1.png":    "fls-sensing-technologies.png",   # FLS types - fuel level sensor technologies
    "2.png":    "fuel-level-sensor-types.png",    # Fuel level sensors types
    "3.png":    "fuel-level-sensor-capacity.png", # FLS - fuel level sensor capacity

    # Sensors setup and configuration
    "1-3.png":  "fuel-level-sensor-creation.png",     # Fuel level sensor creation
    "2-3.png":  "fuel-sensor-settings-parameters.png", # Example of fuel sensor setting with all parameters

    # GPS certification — ISED Canada (formerly IC)
    "ic-2.png":        "ised-canada-logo.png",         # Common certification programs table
    "ic-2-canada.png": "ised-canada-logo-canada.png",  # Canada-specific table (larger version)
    # GPS certification — CSA Canada (sa = Canadian Standards Association)
    "sa-2.png":        "csa-canada-logo.png",          # Common certification programs table
    "sa-2-canada.png": "csa-canada-logo-canada.png",   # Canada-specific table (larger version)

    # Jimi JC400 troubleshooting
    "img1.jpg": "jimi-jc400-troubleshooting-1.jpg",   # Img1 / Jimi JC400 troubleshooting
    "img2.jpg": "jimi-jc400-troubleshooting-2.jpg",   # Img2 / Jimi JC400 troubleshooting

    # Fuel alerts — Settings sub-section
    "image-20230711-085949.png": "fuel-alert-settings-1.png",
    "image-20230711-085906.png": "fuel-alert-settings-2.png",
    "image-20230711-090058.png": "fuel-alert-settings-3.png",
    "image-20230711-090110.png": "fuel-alert-settings-4.png",
    # Fuel alerts — Event reports sub-section
    "image-20230711-090501.png": "fuel-alert-event-report-1.png",
    "image-20230711-090518.png": "fuel-alert-event-report-2.png",

    # LBS/positioning — descriptive replacements for ad_* and hash-named files
    "ad_lbs_hardware.png":    "gsm-cell-tracking-hardware.png",     # GSM based tracking
    "ad_lbs_mobile.png":      "gps-tracking-mobile-app.png",        # GSM and Wi-Fi based tracking in X-GPS apps
    "ad_wifi_hardware-1.png": "rssi-wifi-tracking-hardware.png",    # Received Signal Strength Indicator
    "bc4vohulb7-600x348.png": "mozilla-location-services-coverage.png",  # Mozilla Location Services coverage
    "delay2.png":             "eotd-time-difference-positioning.png",    # E-OTD Enhanced Observed Time Difference
    "test3.png":              "time-of-flight-wifi-positioning.png",     # Time of Flight Wifi location

    # Fuel level sensors — Russian-transliterated screenshot name
    "skrinshot-19-02-2020-102342.png": "fuel-level-sensor-example.png",  # Fuel level sensor example
}


def slugify_check(name: str) -> bool:
    """Basic check: only lowercase letters, digits, hyphens, dots, underscores."""
    return bool(re.match(r'^[a-z0-9][a-z0-9._-]*\.[a-z]+$', name))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    dry_run = args.dry_run
    if dry_run:
        print("=== DRY RUN — no files will be changed ===\n")

    # Validate mapping
    conflicts = []
    for old, new in RENAMES.items():
        new_path = ASSETS / new
        if new_path.exists() and new != old:
            conflicts.append(f"  CONFLICT: {new} already exists (would overwrite)")
        if not (ASSETS / old).exists():
            conflicts.append(f"  MISSING:  {old} not found in assets")
    if conflicts:
        print("Issues found — fix before proceeding:")
        for c in conflicts:
            print(c)
        return

    # Collect all markdown files that might reference these assets
    md_files = list(EC_ROOT.rglob("*.md"))

    renamed_files  = []
    patched_md     = []

    for old, new in sorted(RENAMES.items()):
        old_path = ASSETS / old
        new_path = ASSETS / new

        # Step 1 — rename asset
        if dry_run:
            print(f"  RENAME  {old}  ->  {new}")
        else:
            old_path.rename(new_path)
            renamed_files.append((old, new))

        # Step 2 — update markdown references
        for md_file in md_files:
            text = md_file.read_text(encoding='utf-8')
            # The filename appears as part of a path like:
            #   ../../.gitbook/assets/FNAME
            # We match the bare filename portion to avoid false positives.
            # Match the bare filename only as a complete path component:
            # preceded by '/' and followed by a non-filename delimiter.
            # This prevents "1.png" from matching inside "image (1).png".
            pattern = r'/' + re.escape(old) + r'(?=[)"\'\s<\]\n]|$)'
            if not re.search(pattern, text):
                continue
            updated = re.sub(pattern, '/' + new, text)
            if updated != text:
                count = len(re.findall(pattern, text))
                if dry_run:
                    rel = md_file.relative_to(Path("."))
                    print(f"    PATCH {rel}  ({count} occurrence(s)  {old} -> {new})")
                else:
                    md_file.write_text(updated, encoding='utf-8')
                    patched_md.append(str(md_file.relative_to(Path("."))))

        if dry_run:
            print()

    if not dry_run:
        print(f"Renamed {len(renamed_files)} asset file(s).")
        print(f"Patched {len(set(patched_md))} markdown file(s).")
        print("Done.")


if __name__ == "__main__":
    main()
