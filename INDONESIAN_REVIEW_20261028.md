# Indonesian Legal translation — 2026-10-28

Prepared on `codex/indonesian-legal-20261028`, based on published main `afe0d001ec5cd8cd7dbd835ab2f0e1b7093bcad7`.
Publication authorized by the user on October 28, 2026 after local verification. The approved process is commit, push, PR merge and GitHub Pages deployment, followed by live verification. The PR and Pages workflow record final publication status.

## Scope

Nine standard Indonesian (`id`) pages: legal home, Terms, general Privacy, EEA/UK/Switzerland Privacy, California Privacy, Privacy entry redirect, account/data deletion, child safety and license introduction. Existing language links gain Indonesian destinations preserving policy and region. Terms/Privacy language entry routes recognize `id`, `id-ID` and legacy `in`/`in-ID`. Canonical page language and paths use `id`.

The English Terms, three Privacy variants, deletion, child-safety and license source documents were downloaded from the public site and matched the repository baseline byte for byte. Existing policy bodies and all original third-party license files remain unchanged. Common CSS is reused.

## Content decisions

- Standard Indonesian. Legal text uses the formal address `Anda`; the app's friendly `kamu` tone does not change legal meaning. Product/menu terms match the current app: Ketentuan Layanan, Kebijakan Privasi, Pengaturan > Informasi > Hapus akun, Penghapusan akun dan data, Lisensi.
- The separate Penghapusan akun dan data item opens instructions and does not delete the account.
- Preserve 24-hour report review, backups up to 90 days, shared-chat message retention exceptions, store-handled purchases/refunds and statutory/store exceptions.
- Preserve the published text-filter claim for KO/EN/ES/FR and mixed input. Indonesian UI/Legal translation does not establish Indonesian production filter coverage. Separate Google Cloud Vision SafeSearch image processing and no separate third-party AI moderation API for text remain explicit.
- Preserve existing Legal under-13 scope and the app's separate 14+ agreement wording. No age policy decision is made here.
- Translate existing regional supplements without inventing Indonesia-specific statutory statements or asserting new jurisdictional compliance.
- Keep original licenses/attribution in their original language. Historical audited build identifiers, inventory counts and limits remain unchanged; no new build certification.

## Verification

9 Indonesian pages; 73 total HTML pages; 2,026 internal links/fragments checked. Terms/Privacy/child-safety section, list and table-row parity with English. App-menu labels match current app_id.arb. Original license bytes preserved; 261 notice-data hashes checked. git diff --check passed.

Browser verification results are in `.audit/local-browser.json`: 320/717/1280 CSS-pixel widths, 100%/200% root text size, light/dark themes, actual language-link clicks and browser-language redirects. The full run passed: 73 pages × 12 conditions = 876 render checks, 564 actual language-link clicks, and 44 browser-language redirects. A final targeted check covers the deletion page after terminology alignment. Screenshots and browser profiles in `.audit/` are local evidence, not website assets.

## Limits and preservation

No independent Indonesian native-speaker legal review, jurisdiction-specific legal opinion, physical device or screen-reader verification. Root text enlargement does not certify every OS accessibility setting. Indonesian production moderation is unverified. Local validation does not establish live Indonesian publication; approved deployment and public URL checks are separate.

No app code, Functions, Firebase data, release builds, dependency versions or signed artifacts changed. Original legal checkout and other worktrees retained. `.audit/` must not be staged or published.
