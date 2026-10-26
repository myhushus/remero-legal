# Remero Legal: Spanish locale and moderation disclosure review

Prepared: 2026-10-26. Staged on a separate branch; production publication requires separate approval.

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

## Existing items to recheck at release

- The existing full licenses page references Remero `1.0.0+23`. Current Android release work uses a later version; dependency/license inventory must be regenerated against the actual release source before asserting it is current. This change keeps all original notices intact.
- The existing KO/EN Terms/Privacy deletion paths use `Settings > Delete Account`, while the standalone deletion page uses `Settings > Information > Account and Data Deletion`. Verify the actual current in-app navigation and align all languages before publishing.
- English/Korean source remains the governing drafting reference here; get qualified review of Spanish wording and regional notices before publishing.

## Publication gate (required)

- Confirm the in-house text Moderation runs in **production**, covers the stated KO/EN/ES fields, and fails closed for uncheckable submissions.
- Verify that no separate external AI service receives text for moderation; cloud infrastructure and image moderation remain separately assessed and accurately disclosed.
- Recheck the current app deletion navigation and existing license inventory; preserve all original notices.
- Do not merge this draft PR into `main` before production rollout and final legal/product verification. GitHub Pages publishes `main` automatically. The local DevSSD checkout and its Git staging are not modified by this remote-branch update.
