# Broken link audit — docs/cleanup-orphans-and-link-audit

Run after Stage 1 cleanup, across all 7 GitBook spaces (661 pages, 4,868 links).

> **Update:** the high-confidence findings were fixed on this branch (see
> **Resolution** below). Remaining items are judgment/content calls.

## Resolution

**Fixed:**
- All **4 old-domain `docs.navixy.com` links** (Pass 5) → converted to cross-space
  GitBook links; every target slug verified live via MCP.
- **Eco Driving** cross-space placeholder (Pass 1) → linked to
  `user-guide/guide/fleet-management/eco-driving` (verified live).
- **Broken embedded image** in `default-flow.md` (Pass 3) → the expired GitBook
  CDN URL was replaced with a local `.gitbook/assets/` reference, and the image
  file (deleted in Stage 1 because only the CDN URL referenced it) was restored.

**Left as-is (need a decision):**
- **"Authentication methods"** placeholder (`/broken/pages/BHOdV0TGv4VkuMMeoGcS`,
  2× in `configuring-navixy-mcp-in-cursor.md`) — no such page exists in the
  navixy-mcp space (confirmed via live search). Needs the page restored in
  GitBook or a correct target supplied.
- **Third-party external 404s** (SaskTel, nyce.org.mx, ecommerce.inn.cl, tyntec) —
  external sites restructured; need a replacement URL or removal per page owner.
- **`sms.navixy.com` / `geocoder.navixy.com`** in on-premise `network.md` — these
  are firewall/port hostnames (port 443 outbound targets), not web pages; the 404
  is expected. Optionally render as plain code instead of links.
- **Pass 2's 3 "missing targets"** — false positives: files exist; the checker hit
  Windows `MAX_PATH` on the deep worktree path. Fine in GitBook/Linux.

## Summary

| Pass | Finding | Real / actionable |
|---|---|---|
| 1 — Placeholder / broken internal links | 2 distinct broken targets, 3 occurrences | **2 (real)** |
| 2 — Missing relative targets | 3 flagged | **0** — all false positives (Windows long-path) |
| 3 — External URLs | 264 flagged | **~10 dead (404)** + a few to verify; 231 are bot-blocked (fine) |
| 4 — Cross-space links | 107 links | targets resolve; **3 unverifiable** (unmapped spaces) |
| 5 — Old-domain links | 4 | **4 (real)** |

---

## Pass 1 — Placeholder / broken internal links (REAL)

- `/broken/pages/BHOdV0TGv4VkuMMeoGcS` — link text "Authentication methods"
  - `navixy-mcp/navixy-mcp-server/getting-started/configuring-navixy-mcp-in-cursor.md:12` and `:58`
- `/broken/spaces/446mKak1zDrGv70ahuYZ/pages/XNkW24afnMe547IH7tqf` (cross-space placeholder)
  - `expert-center/vehicle-telematics-technology/can-and-obdii/obd-tracker-fundamentals.md:107`

These are GitBook "broken link" placeholders — the target page was deleted/moved. Need the replacement target.

## Pass 2 — Missing relative targets (NO real issues)

3 entries flagged in `expert-center/SUMMARY.md` (fuel-consumption-meter-installation.md, test-framework-checklist-to-videocameras-in-navixy.md, building-a-video-telematics-test-lab-…md). **All three files exist on disk.** The check failed only because the worktree path + deep nesting exceeds Windows' ~260-char `MAX_PATH`. No action — these resolve fine in GitBook/Linux.

## Pass 3 — External URLs

### Dead (404/410) — actionable
| URL | Location |
|---|---|
| sasktel.com … /m2m, /m2m-device-certification, /m2m-test-kit, …pdf (4 URLs) | expert-center/…/gps-device-certification/certification-in-canada.md:11 |
| nyce.org.mx/catalogodeestandaresnyce/45156-3/ | …/certification-in-mexico-and-latin-america.md:20 |
| ecommerce.inn.cl/nch | …/certification-in-mexico-and-latin-america.md:28 |
| tyntec.com/navixy-integrates-two-way-messaging-powered-tyntec | on-premise/…/sms-gateway-configuration/tyntec.md:9 |
| http://sms.navixy.com | on-premise/…/requirements/network.md:21 |
| http://geocoder.navixy.com | on-premise/…/requirements/network.md:21 |
| 2096203889-files.gitbook.io/…/image-20250403-151042 (3).png | user-guide/guide/account/iot-logic/flow-management/default-flow.md:32 |

The last one is a **broken embedded image** (points at a GitBook CDN URL instead of a local `.gitbook/assets` path) — worth fixing.

### Other broken — verify manually
- `business.bell.ca/...` (2) — HTTP 500, likely temporary
- `location.services.mozilla.com/` — 406 (Mozilla discontinued this service)
- `gps.rcontrol.com.mx/...RCService.svc` — 400 (SOAP endpoint; HEAD not supported)
- `mettax-tracker.navixy.com`, `mettax-tracker.us.navixy.com` — 400 (likely example server URLs)

### Not broken (no action)
- **231 ACCESS-RESTRICTED (403/401)** — pages exist, the bot is blocked (WordPress hotlink protection on `www.navixy.com/wp-content/uploads/*`, marketing-site HEAD blocks, API endpoints needing POST). These render fine for real users.
- **17 UNREACHABLE** — DNS/SSL/timeout; spot-verify if concerned.

## Pass 4 — Cross-space GitBook links

- **82 in-repo targets** (user-guide, expert-center, admin-panel, on-premise, QnA) — all have a matching local file. Caveat: a local file existing does not guarantee the live GitBook slug matches; these were not each MCP-verified.
- **Out-of-repo, live-verified**: `navixy-api` and `iot-logic-api` bases resolve on navixy.com.
- **Unverifiable (3 links, 2 spaces)** — no published base mapping:
  - `oFNFEIINiGFbhi3Px3dE` → dashboard-studio (1 link)
  - `gh5cGQ23uFYTcp7Fj7Yd` → navixy-ai-assistant / navixy-mcp-server (2 links)
  - Supply the published base URLs (or add to `.claude/gitbook-spaces.json`) to verify these.

## Pass 5 — Old-domain links (REAL — `docs.navixy.com` is banned)

| Location | Bad URL | Suggested internal target |
|---|---|---|
| admin-panel/settings/maps/README.md:71 | docs.navixy.com/on-premise/custom-maps | on-premise/…/configuration/maps-and-gis/custom-maps.md |
| admin-panel/settings/service-preferences/regional-settings.md:10 | docs.navixy.com/user-guide/user-prefernces | (search repo — note typo "prefernces") |
| expert-center/…/howen/event-configuration-on-howen-mdvr.md:7 | docs.navixy.com/user-guide/state-field-value/ | user-guide/guide/events-and-notifications/inputs-and-outputs/state-field-value.md |
| expert-center/…/howen/event-configuration-on-howen-mdvr.md:7 | docs.navixy.com/user-guide/report-on-all-events | user-guide/guide/reports/specific-report-details/report-on-all-events.md |
