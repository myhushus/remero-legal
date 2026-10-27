# Remero Legal — French translation review

Prepared 2026-10-27 against published main `c9c12d12a5bb7bf50a12632bfbf994f430dbbce0`.

## Scope and content

- Nine French routes: legal home; Terms v1.0; Privacy v1.0 entry plus global, EEA/UK/Switzerland and California policies; account/data deletion; child safety; license overview.
- French is a translation of the currently published policy, not a new service policy or an announcement of French safety-filter rollout. Existing effective dates remain unchanged; French translation date is identified separately.
- Current production text filtering is described as KO/EN/ES plus mixed input. Separate Cloud Vision SafeSearch image checks, fail-closed text submission, reports and blocking remain accurately distinguished. The app chat's French dev implementation does not establish a French prod deployment.
- The user-confirmed 24-hour report review and maximum 90-day deleted-data backup period are preserved. Shared-chat retention, limited legal/security/accounting retention, store refund handling and consumer-law exceptions are retained.
- Original license/copyright/NOTICE files, dependency inventories and audited historical release version labels are unchanged. French overview links the full inventory and original texts without translating their legal terms.
- App French labels match `Réglages > Informations > Supprimer le compte`; the separate deletion-guidance item is explicitly distinguished. Existing public URLs remain valid.

## Existing product-policy item

Published Terms/Privacy say the service is not intended for children under 13; current app account creation requires age 14. This translation preserves that existing source boundary and does not lower the app age gate or invent a new eligibility decision. A unified eligibility policy remains a separate product/legal review item. Likewise the app's short deletion/refund messages do not supersede the more detailed existing Legal exceptions.

## Navigation and verification

Every existing document exposes the corresponding French page. Regional Privacy language switches preserve region. `/terms/` and `/privacy/` recognize `fr-*` browser locales and retain no-script choices. `/delete/`, `/licenses/` and other stable historical URLs are preserved; explicit French routes are available for the app.

Validation evidence is local under `.audit/`: content-verification.json, local-browser.json, live-browser.json and live-file-verification.json as executed. The existing notice verifier checks local links/fragments and all 261 original evidence-file hashes. French numbered sections, subsection/table/list counts are checked against English; existing policy body bytes are unchanged except locale navigation/entrypoint choices.

No app source, Functions, production data, release binary or app Git staging is changed by this Legal task. A different app chat may be actively working in its own scope. All generation, browser cache and verification files are on DevSSD.

## Limits

No independent French-speaking lawyer/native-speaker review, real iPhone/Android Safari/Chrome run, or VoiceOver/TalkBack session is claimed. Browser layout checks do not certify substantive legal compliance in every French-speaking jurisdiction. No new country-specific policy, production French moderation support, or newly audited app release is asserted by this translation.

## Completed local checks / publication status

- 37 HTML pages; 444 layout conditions (320/717/1280 CSS px × 100%/200% root text × light/dark): PASS, no document-width overflow. Wide tables retain their own horizontal scroll.
- 128 actual language-link clicks and 14 browser-locale redirects, including fr-FR/CA/CH/BE: PASS.
- Existing notice verifier: 994 local links/fragments and 261 original-file hashes PASS.
- French mobile Privacy and deletion screenshots visually inspected.
- Automatic approval review initially held publication for explicit authorization. The user subsequently approved commit, push, PR merge and public deployment on 2026-10-27.
- Live French URL availability and live browser verification are pending publication; local PASS is not reused as a live-site PASS.
