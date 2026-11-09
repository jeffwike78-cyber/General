# Pre-Submission Checklist

Copy into each app's folder and tick everything off before pressing **Submit for Review**.

## Build
- [ ] Built with Xcode 26+ / iOS 26 SDK; deployment target ≥ iOS 13
- [ ] Version (e.g. 1.0.0) and build number incremented
- [ ] No crashes on a real device; tested on the smallest and largest iPhone sizes (simulator OK)
- [ ] Works offline or shows a clear error (no blank screens or infinite spinners)
- [ ] No placeholder text, "lorem ipsum", "beta" or "test" wording anywhere
- [ ] No debug menus, test buttons or hard-coded API keys in the app bundle

## Privacy
- [ ] `PrivacyInfo.xcprivacy` added to the target and accurate
- [ ] All third-party SDKs are on versions that ship their own privacy manifest
- [ ] App Privacy labels in App Store Connect match the manifest and actual behavior
- [ ] Every permission has a specific Info.plist usage string ("to scan receipts", not "needs camera")
- [ ] Permissions requested only when the feature is used, not at launch
- [ ] If tracking across apps/sites: App Tracking Transparency prompt implemented
- [ ] If accounts exist: **in-app account deletion** works
- [ ] If third-party login (Google, Facebook): an equivalent privacy-focused option such as Sign in with Apple is offered

## Payments
- [ ] Paid Apps agreement, banking and tax are active in App Store Connect
- [ ] Digital goods/features are sold through In-App Purchase
- [ ] IAP products are created and **submitted with this version**
- [ ] **Restore Purchases** button exists
- [ ] Paywall shows price, billing period, trial terms, and links to Terms (EULA) and Privacy Policy
- [ ] Subscription tested in the sandbox / TestFlight

## Listing
- [ ] `python3 scripts/check-listing.py` passes
- [ ] Screenshots show the real app (6.9" iPhone required; 13" iPad if the app supports iPad)
- [ ] Privacy Policy URL and Support URL are live (open them in a private window)
- [ ] Age rating questionnaire completed honestly
- [ ] Review notes include a demo login and steps to reach key features

## Final
- [ ] TestFlight build tested by at least one other person
- [ ] Release option chosen: manual release (recommended, so you control the launch day) or automatic
