# Remero Legal publication review — 2026-10-26

Scope: PR #2, KO/EN/ES Terms, global/EEA-UK-Switzerland/California Privacy, account deletion, child safety, license notices and public navigation. User authorized correction, merge into main and GitHub Pages publication. No app code, Functions, data or release build changes are authorized or performed here.

## Operating evidence

- Production rollout result: `approvecontent-00006-lep`, deployed source SHA-256 `8d6431de941f98a4bd83b1fdffb70d6e48f879ebd43d7db3ce7267552342428b`, exact candidate match. Existing rollout evidence records 141 passing authenticated checks, zero failures, 228 existing documents preserved and zero additional external text/image usage during the text smoke. This review reads the evidence; it does not repeat production writes or smoke calls.
- Deployed candidate `contentModerationProvider.ts`: text calls `localTextVerdict` directly without external AI/fallback; images use Google Cloud Vision SafeSearch separately. `contentApproval.ts` includes profile names, Looking For fields, chat snapshots and message text; failed/unavailable checks reject publication.
- Account deletion implementation: `adminAccountDeletionClient.anonymizeChats` clears participant profile snapshots and marks participation deleted; existing message subcollections remain. The public description now states that boundary explicitly in all three languages. No deletion was executed for this review.
- Information flow and localized menu resources confirm Settings > Information > Delete account; Spanish is Configuración > Información > Eliminar cuenta. The separate account/data-deletion link opens instructions only.
- Original license audit remains scoped to Android production +46 and local signed iOS archive 45. All 261 original notice/inventory files remain byte-identical to the PR baseline. No claim that supplemental notices are already included in existing binaries.

## Corrections

- Added explicit Google Cloud Vision image-processing disclosure to all nine Privacy variants; clarified photo processing purposes.
- Added shared-chat retention explanation to all nine Privacy variants and KO/EN/ES deletion guidance.
- Completed missing Korean child-safety page and Korean landing page using existing design and published English policy; preserved original safety contact and policy commitments.
- Corrected Spanish menu labels. Explicit locale navigation prevents browser language from overriding the selected document language; regional language switches preserve the selected region.
- Preserved existing public URLs, exact original license texts, support contacts and current terms. Updated stale pre-publication wording without claiming a new app build.

## Verification

- 28 HTML pages: all local links and fragments resolved; 261 license file hashes verified; inventory checks passed (168 Dart, 161 Android, 21 iOS rows; 147 Android artifact matches and 14 metadata-only rows).
- 199 distinct public external page/source links returned HTTP 200 (HEAD, GET fallback if needed).
- Isolated actual Chrome, all 28 pages at 320 and 1280 CSS pixels, 100% and 200% root text: 112 rendering conditions; no document horizontal overflow or failed images. Normal desktop scrollbar width is allowed.
- 63 exposed language-link clicks and six browser-language redirects checked. Mobile screenshots reviewed for Korean child safety, Spanish regional Privacy and Spanish licenses.
- Keyboard/screen-reader and physical mobile-device testing were not performed. Source/HTML semantic checks and desktop Chrome emulation are not those tests.
- Public-site deployment and post-deployment verification: pending.

## Operator-confirmed operating commitments

On 2026-10-26 the operator explicitly confirmed that both existing commitments remain in effect: reports are reviewed within 24 hours and deleted data remains in backups for at most 90 days. These commitments are retained unchanged. This is operator confirmation, not an independent SLA measurement or backup purge test. Publication is authorized; the operating-confirmation hold is cleared.

## Limits

This is a technical/product consistency and translation review, not a qualified jurisdiction-specific legal opinion. No independent lawyer review, real deletion, support-email delivery, reporting-response SLA measurement, backup purge experiment, App Store-processed IPA audit, new binary build or SDK source-to-binary reproduction was performed. Historical notice-bundling follow-up remains for a future authorized app release.

## Primary public references consulted

- https://support.google.com/googleplay/android-developer/answer/13327111 (deletion resource and retention disclosures)
- https://support.google.com/googleplay/android-developer/answer/14747720 (child-safety public standards and contact)

These support the review criteria, not a claim of blanket legal or store compliance.
