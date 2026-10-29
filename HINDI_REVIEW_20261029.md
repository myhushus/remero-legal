# Remero Hindi Legal review — 2026-10-29

Prepared on `codex/hindi-legal-20261029` from published main `f4446c57adaf79b24e7539bcdb38abe3fdf34c3c`.

Scope: nine Hindi pages (home, Terms, privacy redirect/global/EEA-UK-CH/California, deletion, child safety, licenses); corresponding language switches and Hindi browser-language routing for Terms/Privacy. Existing CSS is reused with a scoped Hindi table-overflow rule; canonical URLs retained; existing-language policy bodies change only for the approved age14 policy and update dates. Original license notices and inventories remain unchanged.

Content: polite Indian Hindi, app terminology aligned with the Hindi app delivery. No new India-specific rights, legal bases, government contacts, data collection, or moderation capability claims introduced. Hindi translation does not establish Hindi backend moderation support. Existing published Korean/English/Spanish/French text filtering disclosures remain as written. Report review within24 hours, backup retention up to90days, shared-chat retention exceptions, store refunds and child safety contacts retained.

Age policy resolved on2026-10-29: user explicitly confirmed that people under14 may not use Remero. Terms and all three privacy variants are updated in all9 languages (36 pages), including references to personal information of under14 users. Updated policy text clearly prohibits use rather than merely saying the service is not intended for a group. Applicable-law capacity requirement remains. No app/backend enforcement or user-data changes performed. The age14 change supersedes the earlier mismatch notes in historical audit files.

Verification: `.audit/content-check.json` and `.audit/local-browser.json`. Independent native-speaker/legal counsel review was not performed. Deployment results will be recorded separately after publishing. Existing signed release artifact audit evidence is reused as published, not re-certified against a new binary. No app runtime, Firebase, prod Functions or Release builds changed. At local preparation, staging/commit/push had not been performed. The user subsequently authorized Legal-only commit/push/PR merge/publication.

Final local QA: 108 Hindi conditions passed after the table fix; 876 existing-language conditions passed in the full run. All718 exposed language-switch tests and48 language redirects passed; final Hindi switches also passed. Internal link/fragment checks2705; original license files262 unchanged. Independent native-speaker/legal review remains unverified.

Age14 final verification: 36 changed pages × widths320/717/1280 × text sizes100%/200% × light/dark =432 browser conditions PASS. No page-level horizontal overflow or broken images observed. Other routing/link results are from the previous full run because this update changes only age text and update dates. This evidence predates the authorized publishing step.
