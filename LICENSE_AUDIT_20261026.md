# Remero open-source notice audit — 2026-10-26

## Scope and immutable release evidence

- Android production `1.0.0+46`: `remero-1.0.0+46-release.aab`, SHA-256 `69c760ef46c8a48c21cce92f4851062ccaf94a0b1a1f2f4ad5ae3389e981f393`.
- Latest local iOS release: signed `Remero-45.xcarchive`, `com.meroviq.remero`, `1.0.0(45)`. App.framework/App SHA-256 `6c45dbcfe8d030f15b2d27236728751c6b875fc6534b9340566e69502b209658`.
- Both release binaries remain unchanged. No new Release build, dependency resolution, deployment or PR merge. Only the required PR #2 Legal commit/push is authorized.
- Legal changes are prepared on PR #2 head `0357ac2d45a3ef138b20a798cd25d4751927d0f2` in an isolated worktree; original Legal main and its index remain clean. This follow-up updates PR #2 with the audited Legal changes; it does not merge or deploy them.

## Findings and corrections

1. Existing Legal inventory was obsolete and published license labels without comprehensive original copyright, license and NOTICE text. Added exact-version originals and source links; preserved the contact, public URLs and existing Terms/Privacy documents.
2. Examined all 168 actual Dart lock entries, including development and unsupported-platform dependencies explicitly distinguished from shipped code. No missing package license text remained in the collected set.
3. Examined 161 Android dependency metadata coordinates. 147 artifact SHA-256 values match the actual AAB dependency metadata; 14 are metadata-only, not claims of bundled executable libraries. Zero digest mismatches. Google/Play proprietary SDK terms are distinguished from open-source licenses rather than blanket-labeled Apache.
4. Examined 16 exact SPM checkout revisions plus five CocoaPods acknowledgement components. Included gRPC/BoringSSL/OpenSSL/SSLeay notices from matching source revisions and native archive notice payloads. Both Package.resolved files remain identical with GoogleUtilities 8.1.2; Podfile.lock matches Pods/Manifest.lock.
5. Spoqa Han Sans Neo font bytes match both release artifacts and current source. Added upstream copyright and SIL OFL 1.1 text. This does not relicense Remero itself under OFL.
6. Added 84 consolidated native/font notice sections to `assets/licenses/native-font-NOTICES.txt` and registered that file using official `flutter.licenses`. Only this approved new runtime file was staged; pre-existing staging and pubspec changes were preserved.

## Verification

- Official Flutter LicenseCollector: PASS; 4,182,118 combined bytes, 405,363 gzip bytes. Actual Flutter test-bundle NOTICES.Z includes font and native/OpenSSL markers.
- Settings information flow / icon layout: 23 tests PASS, including existing public license-link behavior.
- Real isolated Chrome rendering: EN/KO page and ES page, 320/1280px, 100%/200% root font, 12 conditions PASS (EN, KO anchor and ES). Fixed long inline path wrapping on the license page; tables retain contained horizontal scrolling. Screenshots retained in the app audit directory.
- Public data manifest: 261 files with exact per-file byte totals; all SHA-256 values verified. All 753 local links/fragments across 26 HTML pages resolve. All 181 public external source links return HTTP 200 on HEAD requests; no developer home/volume paths or private-key markers in public JSON.
- Original Android AAB and iOS App.framework hashes unchanged. Dart lock matches the production Android release workspace. Existing app staging records and unrelated pubspec edits preserved. Diff whitespace checks on edited configuration/HTML PASS; original upstream legal text is preserved without reformatting.

## Distribution status and remaining limits

- These are verified local corrections, not a claim that the current production distribution already includes them. Public availability requires separately approved Legal publication; the supplemental bundled NOTICE requires the next app build. Existing signed binaries cannot be modified in place.
- An App Store-processed/downloaded IPA was not independently retrieved; iOS evidence is the local signed archive used for build 45.
- Vendor/precompiled proprietary internals were assessed through dependency metadata, original archive notices and matching source licenses, not a reproducible source-to-binary audit. No blanket legal-compliance PASS is asserted for undisclosed vendor internals.
- Actual new native Release execution was not performed; no build was requested or run for this notice-only change.

## PR follow-up corrections

- Aligned KO/EN/ES release scope, native/font links and verification limits; localized the Spanish in-app menu path from the actual ARB.
- Corrected all five SDK source links to Flutter 3.44.0 and fixed the broken flutter_web_plugins 0.0.0 hosted-archive link. The SDK placeholder is not a pub.dev release.
- Filled all five CocoaPods exact versions from the preserved Podfile.lock and refreshed the manifest.
- Updated the prior translation review to retire the obsolete +45-only/161-Dart claims while retaining the production text-moderation publication gate.
- Added reproducible verification: `python3 scripts/verify-license-notices.py` (no downloads, builds or writes).

## Primary implementation references

- https://docs.flutter.dev/tools/pubspec#licenses-field
- https://developers.google.com/android/guides/opensource
- https://github.com/spoqa/spoqa-han-sans/blob/main/LICENSE

## Review files

- App: `assets/licenses/native-font-NOTICES.txt`, `pubspec.yaml` (only the added licenses registration belongs to this audit).
- Legal: `public/licenses/index.html`, `public/licenses/es/index.html`, `public/licenses/data/`, this report.
- Per-file hashes, inventories and original texts: `public/licenses/data/manifest.json` and linked inventory files.
