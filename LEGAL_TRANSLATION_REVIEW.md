# Remero Legal: Spanish locale and moderation disclosure review

Prepared: 2026-10-26. Historical preparation review. The user subsequently authorized final corrections, PR merge and Pages publication after production text-filter rollout. See `PUBLICATION_REVIEW_20261026.md` for the current checks and remaining limits.

## Coverage

- Spanish: Terms v1.0; Privacy v1.0 (global, EEA/UK/Switzerland, California); account deletion; child safety; license overview; legal landing page.
- Original license notices are linked unchanged in their original language.
- KO/EN source pages remain accessible and gain Spanish locale links. Terms and Privacy landing pages recognize `es*` browser languages.

## Moderation transparency

- Terms section 6 now explicitly describes Remero's own KO/EN/ES server-side text filter, rejection when checks fail, false-positive limitations, and unchanged image moderation, reports, and blocking.
- Privacy section 5 (KO/EN/ES, including regional variants) now describes the in-house backend checks, mixed-language/obfuscated text, blocked submissions, retries, and continued infrastructure-provider processing. California notices also acknowledge moderation as a processing purpose.
- This proposed text-processing disclosure states that a separate external AI text-moderation API is not used. **It must not be published until the production backend really uses the in-house filter and no longer calls that API for text.**
- Before publication, verify the actual production text request/data flows, service providers, rejection and retry UX, and unchanged image moderation. Do not conflate external cloud infrastructure with an external AI text-moderation API.

## Review and deployment

- Spanish content translates the existing v1.0 source and regional qualifiers; it is not independent legal advice. Review jurisdictional applicability, dates, and actual product behavior before publication.
- Existing KO/EN Terms have a targeted section 6 clarification; existing KO/EN Privacy has targeted section 5 clarification and necessary California-purpose alignment. No existing terms, safety actions, or license source inventory was removed.
- GitHub Pages workflow deploys from `main` only, so this feature branch does not publish the website.

## Account-deletion path and license audit (2026-10-26)

- App source `myhushus/remero`, branch `codex/premium-share-release-45-20261022`, confirms **Settings > Information > Delete account** is the account deletion action. The separate **Account and Data Deletion** item opens `/delete/` and does not delete the account. KO/EN/ES Terms, regional Privacy, and the account-deletion instructions have been aligned. Recheck actual localized labels and flow on the production +46 build.
- License v1.3 supersedes the earlier +23/+45-only inventory. The actual Android production +46 AAB, iOS build 45 signed release archive, and unchanged lockfiles were audited: 168 resolved Dart/Flutter entries; 161 Android metadata coordinates (147 artifact SHA-256 matches, 14 metadata-only); 16 SPM checkouts and five CocoaPods components. Original license/copyright/NOTICE files and Spoqa font OFL text are included with a verified SHA-256 manifest.
- The App Store-processed IPA and opaque precompiled SDK internals remain outside the verified scope. See `LICENSE_AUDIT_20261026.md`; do not describe the local corrections as already deployed or included in existing signed binaries.
- English/Korean source remains the governing drafting reference here; obtain final qualified review of the Spanish wording and regional notices before publishing.

## Publication gate (required)

- Confirm the in-house text Moderation runs in **production**, covers the stated KO/EN/ES fields, and fails closed for uncheckable submissions.
- Verify that no separate external AI service receives text for moderation; cloud infrastructure and image moderation remain separately assessed and accurately disclosed.
- The +46 AAB/native inventory and local iOS archive notice audit are complete within the stated limits. Confirm the localized account-deletion UX and remaining publication gates; retain original attribution texts and include supplemental NOTICE in the next app build.
- Do not merge this draft PR into `main` before production rollout and final legal/product verification. GitHub Pages publishes `main` automatically. The app checkout and its Git staging remain unchanged; only the isolated Legal worktree is committed/pushed.
