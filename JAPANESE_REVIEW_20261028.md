# Japanese Legal translation — 2026-10-28

Prepared on `codex/japanese-legal-20261028`, based on published main `b50f76945d4b3c4da896b5e1d84ec41c5c5a77c0`.
Publication authorized by the user on October 28, 2026 after local verification. The approved process is commit, push, PR merge and GitHub Pages deployment, followed by live-site verification. The PR and Pages workflow record the final publication status.

## Scope

Nine Japanese pages: legal home, Terms, general Privacy, EEA/UK/Switzerland Privacy, California Privacy, Privacy entry redirect, account/data deletion, child safety and license introduction. Existing language navigation gains Japanese links preserving the selected policy/region. `/privacy/` and `/terms/` recognize browser locales `ja` and `ja-JP`. Existing public URLs remain unchanged.

The English Terms, three regional Privacy documents, deletion, child-safety and license source pages were downloaded from the public site and matched the repository baseline byte for byte. Existing policy bodies and original third-party license files remain unchanged. The current common CSS is reused.

## Content decisions

- Standard Japanese; app menu labels match the delivered Japanese app strings: 設定 > 情報 > アカウントを削除. The separate アカウントとデータの削除 item opens guidance and does not delete the account.
- Preserve 24-hour report review, backups up to 90 days, shared-chat message retention exceptions, store-handled purchases/refunds and statutory/store exceptions.
- Preserve the published text-filter claim for KO/EN/ES/FR and mixed input. Japanese translation does not establish Japanese production filter coverage. Separate Google Cloud Vision SafeSearch image processing and no separate third-party AI moderation API for text remain explicit.
- Preserve existing Legal under-13 scope and the app's separate 14+ agreement wording. No age eligibility policy is changed here.
- Translate existing regional supplements; do not invent a Japan-specific statutory policy or assert new jurisdictional compliance.
- Keep original licenses and attribution text in their original language. Japanese license introduction retains the exact historical audited build identifiers, inventory counts and verification limits; it does not certify a new build.

## Verification

Content/link verification: 9 Japanese pages; 64 total HTML pages; 1,741 local links/fragments checked. All numbered sections, list items and table row structures in Terms/Privacy/child-safety correspond to source. App menu labels match the Japanese translation package. Original license file bytes preserved; 261 notice data hashes checked by the repository verifier. `git diff --check` passed.

Browser PASS: 64 pages × 12 conditions = 768 render checks; 428 actual language-link clicks and 36 locale redirects passed. Results are recorded in `.audit/local-browser.json`: 320/717/1280 CSS-pixel widths, 100%/200% root text size, light/dark themes, actual language-link clicks and browser-language redirects. Screenshots are in `.audit/` and are local verification artifacts, not site assets.

## Limits and preservation

No independent Japanese native-speaker legal review or jurisdiction-specific legal opinion. No physical device/VoiceOver/TalkBack validation. Browser root text enlargement is not a claim of every OS accessibility configuration. No Japanese production moderation verification. Local checks do not establish live Japanese publication; that requires approved deployment and live URL checks.

No app runtime, Functions, Firebase data, release build, dependency version or signed artifact changes. Original legal checkout and existing worktrees retained. `.audit/` contains local scripts, browser profiles and evidence and must not be staged or published.
