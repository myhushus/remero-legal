# Remero Portuguese Legal review

Prepared against published main `b85f8db77c465346b98bb97e4ba7dcf3dc5924ca` on 2026-10-28.

## Scope

Nine Portuguese routes: `/pt/`, Terms v1.0, Privacy v1.0 entry and global/EEA-UK-Switzerland/California policies, account/data deletion, child safety and license overview. Writing uses Brazilian Portuguese with broadly understandable terms. The URL language is `pt`; document language is `pt-BR`. This is not a separate pt-PT translation or a new Brazil-specific legal policy.

Existing effective dates and product obligations are preserved. The 24-hour report review and maximum 90-day deleted-data backup period were confirmed by the user earlier in this conversation. Shared chat messages and necessary security/legal/accounting retention exceptions remain explicit. Store refunds remain subject to applicable store terms and mandatory law. Original license/copyright/NOTICE materials and historical audited release labels remain unchanged.

Portuguese app labels match the prepared app ARB: `Configurações > Informações > Apagar conta`. The separate `Remoção da conta e dos dados` item opens instructions rather than deleting the account. Production app availability in Portuguese is not certified by this website task.

## Verified operational correction

The local production deployment record for 2026-10-28 reports successful French filter rollout to revision `approvecontent-00007-cis`, with 135 smoke cases passing and zero changes to 276 existing records. Evidence was read from the app's `runtime/reports/moderation/fr-prod/2026-10-28/runs/fr-approved-20261028/prod-deployment-result.json` and `prod-final-result.json` without modifying app files.

Existing KO/EN/ES/FR Terms and Privacy therefore gain French in the enumerated production text-filter languages, with the update date advanced to October 28. Portuguese content describes the same KO/EN/ES/FR coverage. Portuguese filter production support is not asserted. No production Functions, data, or app builds were changed by this task.

## Checks

- Numbered section, subsection, table, row/cell and list parity with English: five document comparisons passed (Terms, three Privacy policies, Child Safety).
- Existing policy bodies are unchanged except the exact verified French coverage correction and dates; other edits add Portuguese navigation and entry choices.
- 46 HTML pages, 1,225 internal links/fragments, 261 original evidence hashes: passed the repository notice verifier.
- Original license evidence files are byte-for-byte unchanged.
- Portuguese deletion and global privacy at 320px visually reviewed.
- Browser matrix and real language-link click results: `.audit/local-browser.json` once complete. These are local browser checks, not public-site results.

## Remaining scope

Commit, push, PR, merge and public deployment have not been performed for this Portuguese change. Public URL checks follow publication; local checks cannot certify the live site.

Independent Portuguese-speaking legal/native-speaker review, actual iPhone/Android testing and VoiceOver/TalkBack testing were not performed. This translation does not certify compliance in every Portuguese-speaking jurisdiction or create a new LGPD-specific policy.

The existing Legal under-13 boundary and app account-creation minimum age 14 remain an explicit separate product/legal policy alignment item. The translation preserves the published boundary without changing the app's age gate.

## Completed browser verification

Local Chrome checks passed: 552 layout conditions across 46 pages (320/717/1280 CSS px × 100%/200% root text × light/dark), 210 actual language-link clicks and 24 browser-locale redirects including pt, pt-BR, pt-PT, pt-AO and pt-MZ. No document-width overflow; wide tables retain their own scrolling. Evidence: `.audit/local-browser.json`. Public deployment remains pending authorization.

The user explicitly approved commit, push, PR merge and public deployment in this conversation after the completed local review. Publication results will be recorded separately after live verification.
