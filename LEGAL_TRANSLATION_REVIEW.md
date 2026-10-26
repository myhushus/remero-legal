# Remero Legal: Spanish locale and moderation disclosure review

Prepared: 2026-10-26. Staged on a separate branch; production publication requires separate approval.

## Coverage

- Spanish: Terms v1.0; Privacy v1.0 (global, EEA/UK/Switzerland, California); account deletion; child safety; license overview; legal landing page.
- Original license notices are linked unchanged in their original language.
- KO/EN source pages remain accessible and gain Spanish locale links. Terms and Privacy landing pages recognize `es*` browser languages.

## Moderation transparency

- Terms section 6 already describes automated filtering and manual moderation.
- Privacy section 5 now explicitly describes automated checks of submitted text for prohibited/abusive expressions and review of reports in KO, EN, and ES.
- The disclosure is provider-neutral and does **not** claim external moderation services have already been removed from production.
- Before publication, compare text moderation paths with this description and verify whether Privacy section 6 needs to identify any external moderation processor.

## Review and deployment

- Spanish content translates the existing v1.0 source and regional qualifiers; it is not independent legal advice. Review jurisdictional applicability, dates, and actual product behavior before publication.
- Existing KO/EN Terms are unchanged. Existing KO/EN Privacy has only section 5 disclosure/update date and locale links updated.
- GitHub Pages workflow deploys from `main` only, so this feature branch does not publish the website.
