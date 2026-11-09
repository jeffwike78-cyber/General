# Repo guide for Claude

This repo is an iOS app portfolio. Every app lives in `apps/<slug>/`, created with `scripts/new-app.sh`.
The playbook is `app-store-kit/README.md`; follow it.

## Rules for any app work
- Before building, make sure `apps/<slug>/app-brief.md` is filled in. If it isn't, help the owner fill it in first.
- Target the current Apple requirements: Xcode 26+ / iOS 26 SDK, deployment target ≥ iOS 13. Recheck developer.apple.com/news/upcoming-requirements when unsure.
- Keep `PrivacyInfo.xcprivacy`, Info.plist usage strings and the privacy policy in sync with what the code actually collects.
- If an app has accounts, it must include in-app account deletion.
- Paywalls: price, period, trial terms, Restore Purchases, and Terms + Privacy links.
- Each app must be clearly distinct from the others (Guideline 4.3). Share code modules, not whole app concepts.
- Run `python3 scripts/check-listing.py apps/<slug>/store-listing.md` after editing a listing.
- Never commit `.p8` keys, certificates, provisioning profiles or API secrets.
- On a Mac with the Xcode plugin (`/plugin install xcode@claude-plugins-official`), build and run in the simulator to verify changes before calling them done.
