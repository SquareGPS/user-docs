"""
recover_expert_center_images.py

Recovers broken Expert Center images from a Confluence markdown export.

The export file embeds images as base64-encoded PNG data URIs:
    ![alt text][imageN]                          <-usage line
    [imageN]: <data:image/png;base64,...>        <-definition line

Broken image URLs in the repo look like:
    https://www.navixy.com/wp-content/uploads/YYYY/MM/filename.ext

The script:
  1. Parses the export MD to build imageN → (png_bytes, alt_text, section_heading)
  2. Collects all broken navixy.com/wp-content/uploads URLs from the repo
  3. Matches export images to broken URLs via alt text (exact → fuzzy → section+position)
  4. Saves matched images to docs/expert-center/.gitbook/assets/
  5. Patches markdown files to use local relative paths

Usage:
    python scripts/recover_expert_center_images.py --dry-run   # no changes, print plan
    python scripts/recover_expert_center_images.py             # execute
"""

import re
import base64
import difflib
import argparse
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
EXPORT_MD  = Path(r"C:\Users\andre\Downloads\Expert Center-v8-20250417_084027.docx.md")
REPO_ROOT  = Path(r"C:\Users\andre\repos\user-docs")
EC_ROOT    = REPO_ROOT / "docs" / "expert-center"
ASSETS     = EC_ROOT / ".gitbook" / "assets"
LOG_FILE   = REPO_ROOT / "unmatched_images.log"

# ── Patterns ───────────────────────────────────────────────────────────────────
# Matches base64 image definition lines:  [imageN]: <data:image/png;base64,DATA>
DEFN_RE  = re.compile(r'^\[image(\d+)\]:\s*<data:image/png;base64,([A-Za-z0-9+/=\s]+)>', re.MULTILINE)

# Matches image usage lines:  ![alt text][imageN]  (anywhere on the line)
USE_RE   = re.compile(r'!\[([^\]]*)\]\[image(\d+)\]')

# Matches heading lines: ## heading  or  ### heading  etc.
HDG_RE   = re.compile(r'^#{1,6}\s+(.+)')

# Matches broken navixy WP URLs in markdown (both inline and HTML forms)
# Groups: (1) full URL, (2) bare filename
BROKEN_URL_RE = re.compile(
    r'(https?://(?:www\.)?navixy\.com/wp-content/uploads/\d{4}/\d{2}/([^)\s"\'<\]\n]+))',
    re.IGNORECASE,
)

# NOTE: we keep original WP file extensions (even though export data is always PNG)
# to avoid filename collisions, e.g. 1.jpg and 1.png would both normalise to 1.png.
# Browsers and GitBook render by content, not extension, so .jpg files with PNG
# data display correctly.

# ── Section → file mapping ──────────────────────────────────────────────────────
# Maps export section headings (lowercase, stripped) to repo file path suffixes.
# Used as fallback when alt-text matching fails.
# A section can map to multiple files (split by sub-headings); order matters for
# position-based matching within the section.
SECTION_FILE_MAP = {
    # ── Positioning / connectivity / sensors ────────────────────────────────
    "what is lbs tracking: cell id and wps": [
        "vehicle-telematics-technology/positioning-techniques/what-is-lbs-tracking-cell-id-and-wps.md"
    ],
    "mqtt fundamentals": [
        "vehicle-telematics-technology/connectivity/mqtt-fundamentals.md"
    ],
    "wireless telematics sensors": [
        "vehicle-telematics-technology/vehicle-sensors/wireless-telematics-sensors.md"
    ],
    # ── Fuel: sensors setup (sub-headings used for position matching) ───────
    "sensors setup and configuration": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/sensors-setup-and-configuration.md"
    ],
    "adding calibration data": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/sensors-setup-and-configuration.md"
    ],
    # ── Fuel: alerts (sub-headings Settings / Event reports) ────────────────
    "fuel level change": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/analyzing-fuel-data/fuel-alerts-and-notifications.md"
    ],
    "settings": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/analyzing-fuel-data/fuel-alerts-and-notifications.md"
    ],
    "event reports": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/analyzing-fuel-data/fuel-alerts-and-notifications.md"
    ],
    # ── Fuel: widgets ────────────────────────────────────────────────────────
    "fuel related widgets": [
        "vehicle-telematics-technology/fuel-management/fuel-control-in-navixy/analyzing-fuel-data/fuel-related-widgets.md"
    ],
    # ── Fuel: level sensors ──────────────────────────────────────────────────
    "fuel level sensors": [
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-level-sensors/README.md",
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-level-sensors/types-of-fuel-level-sensors.md",
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-level-sensors/fuel-level-sensor-installation.md",
    ],
    "liquid level sensing technologies": [
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-level-sensors/README.md",
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-level-sensors/types-of-fuel-level-sensors.md",
    ],
    # ── Fuel: flow meters ────────────────────────────────────────────────────
    "fuel flow meters": [
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-flow-meters/README.md",
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-flow-meters/types-of-fuel-flow-meters.md",
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-flow-meters/fuel-flow-meter-installation.md",
    ],
    "flow meter installation routine": [
        "vehicle-telematics-technology/fuel-management/installation-and-initial-configuration-of-fuel-control-devices/fuel-flow-meters/fuel-flow-meter-installation.md"
    ],
    # ── CAN / OBD ────────────────────────────────────────────────────────────
    "intra-vehicle communication: can, flexray, and most": [
        "vehicle-telematics-technology/can-and-obdii/intra-vehicle-communication-can-flexray-and-most.md"
    ],
    "obd tracker fundamentals": [
        "vehicle-telematics-technology/can-and-obdii/obd-tracker-fundamentals.md"
    ],
    # ── Certification ────────────────────────────────────────────────────────
    "gps device certification": [
        "vehicle-telematics-technology/legistlation/gps-device-certification/README.md",
        "vehicle-telematics-technology/legistlation/gps-device-certification/certification-in-us.md",
        "vehicle-telematics-technology/legistlation/gps-device-certification/certification-in-canada.md",
        "vehicle-telematics-technology/legistlation/gps-device-certification/certification-in-mexico-and-latin-america.md",
    ],
    # ── Video telematics ─────────────────────────────────────────────────────
    "dash cam installation": [
        "vehicle-telematics-technology/video-telematics/dash-cam-installation.md"
    ],
    "jimi jc400 troubleshooting": [
        "vehicle-telematics-technology/video-telematics/configuration-guides/jimi-iot/jimi-jc400-troubleshooting.md"
    ],
    # ── FAQ / Manage Sensors ─────────────────────────────────────────────────
    "manage sensors": [
        "faq-and-troubleshooting/sensors/manage-sensors.md"
    ],
    "discrepancies between the real values and the values received from the sensor": [
        "faq-and-troubleshooting/sensors/manage-sensors.md"
    ],
}


# ══════════════════════════════════════════════════════════════════════════════
# Step 1 — Parse the markdown export
# ══════════════════════════════════════════════════════════════════════════════

def parse_export(path: Path) -> dict:
    """
    Returns:
        images: dict  imageN (str) → {'data': bytes, 'alt': str, 'section': str}
    """
    text = path.read_text(encoding='utf-8')

    # Pass 1: collect base64 data for each imageN
    data_map = {}
    for m in DEFN_RE.finditer(text):
        n, b64 = m.group(1), m.group(2)
        # Remove any whitespace that may have been inserted
        b64_clean = re.sub(r'\s+', '', b64)
        try:
            data_map[n] = base64.b64decode(b64_clean)
        except Exception as e:
            print(f"  [warn] Could not decode image{n}: {e}")

    # Pass 2: walk lines, track headings, record first usage and ALL alts per imageN
    alt_map     = {}   # imageN → alt text (first occurrence, for section tracking)
    section_map = {}   # imageN → section heading at time of first usage
    all_alts    = {}   # imageN → set of all alt texts seen across all occurrences
    current_heading = ""

    for line in text.splitlines():
        # Strip leading whitespace and ordered-list markers (e.g. "  1. ")
        # Export headings often appear as "  1. ## **Heading** {#anchor}"
        stripped = re.sub(r'^\s*(?:\d+\.\s+)*', '', line)
        hdg_m = re.match(r'^(#{1,6})\s+(.+)', stripped)
        if hdg_m:
            raw = hdg_m.group(2).strip()
            raw = re.sub(r'\*+', '', raw)          # remove **bold** markers
            raw = re.sub(r'\{[^}]+\}', '', raw)    # remove {#anchor} tags
            raw = re.sub(r'\\\.', '.', raw)        # unescape \. sequences
            current_heading = raw.strip()

        for use_m in USE_RE.finditer(line):
            alt, n = use_m.group(1).strip(), use_m.group(2)
            # Track first occurrence for section assignment
            if n not in alt_map:
                alt_map[n]     = alt
                section_map[n] = current_heading
            # Track ALL alt texts for this imageN (handles repeated images)
            all_alts.setdefault(n, set())
            if alt:
                all_alts[n].add(alt)

    # Merge
    images = {}
    for n, data in data_map.items():
        images[n] = {
            'data':     data,
            'alt':      alt_map.get(n, ''),
            'section':  section_map.get(n, ''),
            'all_alts': all_alts.get(n, set()),
        }

    print(f"[export] parsed {len(images)} image definitions, "
          f"{len(alt_map)} usages")
    return images


# ══════════════════════════════════════════════════════════════════════════════
# Step 2 — Collect broken URLs from the repo
# ══════════════════════════════════════════════════════════════════════════════

def collect_broken_urls(ec_root: Path) -> list:
    """
    Returns list of dicts:
        {'file': Path, 'alt': str, 'url': str, 'filename': str, 'line_no': int}
    Deduplicated by (file, url) — same URL may appear on multiple lines in one file.
    """
    entries = []
    seen = set()  # (file, url) pairs already recorded

    for md_file in sorted(ec_root.rglob('*.md')):
        text = md_file.read_text(encoding='utf-8')
        for line_no, line in enumerate(text.splitlines(), 1):
            for m in BROKEN_URL_RE.finditer(line):
                url, filename = m.group(1), m.group(2)
                # Skip PDF links — they're download links, not images
                if filename.lower().endswith('.pdf'):
                    continue
                key = (str(md_file), url)
                if key in seen:
                    continue
                seen.add(key)

                # Extract alt text from markdown syntax on this line
                alt = ''
                # Try ![alt](url)
                alt_m = re.search(r'!\[([^\]]*)\]\(' + re.escape(url), line)
                if alt_m:
                    alt = alt_m.group(1).strip()
                # Try <img ... alt="alt" ...> (order: before or after src)
                if not alt:
                    img_alt_m = re.search(r'<img\b[^>]*\balt=["\']([^"\']*)["\']', line, re.IGNORECASE)
                    if img_alt_m:
                        alt = img_alt_m.group(1).strip()

                entries.append({
                    'file':     md_file,
                    'alt':      alt,
                    'url':      url,
                    'filename': filename,
                    'line_no':  line_no,
                })

    print(f"[repo]   found {len(entries)} unique broken URL occurrences "
          f"in {len({e['file'] for e in entries})} files")
    return entries


# ══════════════════════════════════════════════════════════════════════════════
# Step 3 — Match export images to broken URLs
# ══════════════════════════════════════════════════════════════════════════════

def _norm(s: str) -> str:
    """Normalise string for comparison."""
    return re.sub(r'\s+', ' ', s).strip().lower()


def match_images(images: dict, broken_urls: list) -> tuple:
    """
    Returns:
        matches:   list of (broken_url_entry, imageN, match_method)
        unmatched: list of broken_url_entry
    """
    # Build lookup by normalised alt text — use ALL alt texts per imageN so that
    # images referenced multiple times with different alt texts are discoverable
    alt_to_ns = {}  # norm_alt → [imageN, ...]
    for n, img in images.items():
        for alt in img.get('all_alts', set()) | ({img['alt']} if img['alt'] else set()):
            key = _norm(alt)
            if key and n not in alt_to_ns.get(key, []):
                alt_to_ns.setdefault(key, []).append(n)

    # Build section → ordered list of imageNs (for position matching)
    section_to_ns = {}
    for n, img in images.items():
        key = _norm(img['section'])
        section_to_ns.setdefault(key, []).append(n)
    # Sort by numeric imageN within each section
    for k in section_to_ns:
        section_to_ns[k].sort(key=lambda x: int(x))

    # Track which imageNs have already been used (for position matching)
    used_ns = set()

    # Group broken URLs by file for position-based fallback
    file_urls = {}
    for entry in broken_urls:
        file_urls.setdefault(str(entry['file']), []).append(entry)

    matches   = []
    unmatched = []

    # --- file-level section inference (for position matching) ---
    def infer_sections_for_file(file_path: Path) -> list:
        """All export section keys that map to this repo file (insertion order)."""
        rel = str(file_path.relative_to(EC_ROOT)).replace('\\', '/')
        result = []
        for section_key, files in SECTION_FILE_MAP.items():
            if any(rel.endswith(f) or rel == f for f in files):
                result.append(section_key)
        return result

    for entry in broken_urls:
        alt  = _norm(entry['alt'])
        url  = entry['url']
        matched_n      = None
        match_method   = ''

        # 1. Exact alt text match
        if alt and alt in alt_to_ns:
            candidates = [n for n in alt_to_ns[alt] if n not in used_ns]
            if candidates:
                matched_n    = candidates[0]
                match_method = 'exact-alt'

        # 2. Fuzzy alt text match
        if not matched_n and alt:
            all_alts_keys = list(alt_to_ns.keys())
            close = difflib.get_close_matches(alt, all_alts_keys, n=1, cutoff=0.80)
            if close:
                candidates = [n for n in alt_to_ns[close[0]] if n not in used_ns]
                if candidates:
                    matched_n    = candidates[0]
                    match_method = f'fuzzy-alt({close[0]!r})'

        # 3. Section + position fallback — try each section mapped to this file in order.
        # Always take pool[0] (first unused in document order); used_ns prevents reuse.
        if not matched_n:
            for sec_key in infer_sections_for_file(entry['file']):
                pool = [n for n in section_to_ns.get(sec_key, []) if n not in used_ns]
                if pool:
                    matched_n    = pool[0]
                    match_method = f'section-pos({sec_key!r})'
                    break

        if matched_n:
            used_ns.add(matched_n)
            matches.append((entry, matched_n, match_method))
        else:
            unmatched.append(entry)

    print(f"[match]  matched {len(matches)}, unmatched {len(unmatched)}")
    return matches, unmatched


# ══════════════════════════════════════════════════════════════════════════════
# Step 4 — Save images to .gitbook/assets
# ══════════════════════════════════════════════════════════════════════════════

def _asset_filename(wp_filename: str) -> str:
    """Return the .gitbook/assets filename for a given WP bare filename.
    Keeps original extension to avoid cross-type collisions (e.g. 1.jpg vs 1.png).
    """
    return wp_filename


def save_assets(matches: list, images: dict, dry_run: bool) -> dict:
    """
    Decode and save matched images.
    Returns: url → asset_filename  (for use in patching step)
    """
    url_to_asset = {}
    saved = skipped = 0

    for entry, n, method in matches:
        wp_filename  = entry['filename']
        asset_name   = _asset_filename(wp_filename)
        asset_path   = ASSETS / asset_name
        url_to_asset[entry['url']] = asset_name

        if asset_path.exists():
            skipped += 1
            if dry_run:
                print(f"  SKIP (exists) {asset_name}  <-{wp_filename}  [{method}]")
        else:
            saved += 1
            if dry_run:
                print(f"  SAVE  {asset_name}  <-image{n} alt={entry['alt']!r}  [{method}]")
            else:
                asset_path.write_bytes(images[n]['data'])

    print(f"[assets] {'would save' if dry_run else 'saved'} {saved}, "
          f"skipped {skipped} (already exist)")
    return url_to_asset


# ══════════════════════════════════════════════════════════════════════════════
# Step 5 — Patch markdown files
# ══════════════════════════════════════════════════════════════════════════════

def _rel_prefix(md_file: Path) -> str:
    """
    Compute the relative path prefix from md_file's directory to
    docs/expert-center/.gitbook/assets.
    """
    depth = len(md_file.relative_to(EC_ROOT).parts) - 1  # -1 for the filename itself
    return '/'.join(['..'] * depth) + '/.gitbook/assets'


def patch_markdown(matches: list, url_to_asset: dict, dry_run: bool):
    """Replace broken URLs with local relative paths in all affected files."""
    # Group matches by file
    file_changes = {}
    for entry, n, method in matches:
        file_changes.setdefault(str(entry['file']), []).append(entry)

    patched_files = 0
    patched_lines = 0

    for file_str, entries in file_changes.items():
        md_file  = Path(file_str)
        prefix   = _rel_prefix(md_file)
        original = md_file.read_text(encoding='utf-8')
        updated  = original

        for entry in entries:
            url        = entry['url']
            asset_name = url_to_asset.get(url)
            if not asset_name:
                continue

            new_path = f"{prefix}/{asset_name}"

            # Replace all occurrences of this URL in the file
            count  = updated.count(url)
            if count:
                updated = updated.replace(url, new_path)
                patched_lines += count

        if updated != original:
            patched_files += 1
            if dry_run:
                rel = md_file.relative_to(REPO_ROOT)
                print(f"  PATCH {rel}  ({len(entries)} URL(s) -> {prefix}/...)")
            else:
                md_file.write_text(updated, encoding='utf-8')

    print(f"[patch]  {'would patch' if dry_run else 'patched'} "
          f"{patched_files} files, {patched_lines} URL occurrences")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true',
                        help='Print plan without making any changes')
    args = parser.parse_args()

    dry_run = args.dry_run
    if dry_run:
        print("=== DRY RUN - no files will be changed ===\n")

    print("-- Step 1: Parse export --")
    images = parse_export(EXPORT_MD)

    print("\n-- Step 2: Collect broken URLs --")
    broken_urls = collect_broken_urls(EC_ROOT)

    print("\n-- Step 3: Match images --")
    matches, unmatched = match_images(images, broken_urls)

    print("\n-- Step 4: Save assets --")
    if dry_run:
        print("  (listing planned saves)")
    url_to_asset = save_assets(matches, images, dry_run)

    print("\n-- Step 5: Patch markdown --")
    if dry_run:
        print("  (listing planned patches)")
    patch_markdown(matches, url_to_asset, dry_run)

    # Write unmatched log
    if unmatched:
        log_lines = [
            f"{e['file'].relative_to(REPO_ROOT)} | {e['url']} | alt={e['alt']!r}"
            for e in unmatched
        ]
        if not dry_run:
            LOG_FILE.write_text('\n'.join(log_lines) + '\n', encoding='utf-8')
        print(f"\n[unmatched] {len(unmatched)} URLs could not be matched:")
        for line in log_lines:
            print(f"  {line}")
    else:
        print("\n[unmatched] none — all broken URLs matched successfully!")

    print("\nDone." if not dry_run else "\nDry run complete.")


if __name__ == '__main__':
    main()
