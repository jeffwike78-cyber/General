# App Store Launch Kit

A reusable pipeline for shipping **many** iOS apps with the fewest manual steps.
Do the one-time setup once, then every new app is: `scripts/new-app.sh <name>` → build → fill in templates → upload.

---

## Part 1 — One-time setup (do once, reuse for every app)

### 1. Decide: Individual or Organization (LLC) account
| | Individual | Organization (LLC) — **recommended** |
|---|---|---|
| Cost | $99/yr | $99/yr + LLC filing fee (state-dependent) |
| Seller name on App Store | Your personal legal name | Your company name |
| Liability | Personal | Limited to the LLC |
| Extra requirement | None | Free D-U-N-S number (can take 1–2 weeks) |

Since you plan several apps, enroll as an **LLC**: it hides your personal name, keeps one brand across apps, and keeps revenue separate for taxes. Request the D-U-N-S number now because it's the slowest step.

### 2. Enroll and set up money
1. Enroll at developer.apple.com/programs ($99/yr).
2. In App Store Connect → **Business**: sign the Paid Apps agreement, add bank and tax info. **Paid apps and in-app purchases won't go live until this is done.**
3. Apply for the **App Store Small Business Program**. It cuts Apple's commission from 30% to 15% while your proceeds stay under $1M/yr. It isn't automatic, so apply on day one.

### 3. Create an App Store Connect API key (enables automation)
App Store Connect → Users and Access → Integrations → **App Store Connect API** → generate a key with the *App Manager* role. Download the `.p8` file **once** (you can't download it again) and store it in a password manager. **Never commit it to git.**
Then fastlane / GitHub Actions can upload builds and metadata with no logins or 2FA prompts.

### 4. Pick your build path (do you have a Mac?)
| Path | Needs a Mac? | Best for |
|---|---|---|
| **A. Native Swift + Xcode plugin for Claude Code** | Yes (latest Xcode) | Best quality and performance; Claude builds, runs and fixes it on your Mac |
| **B. Expo / React Native + EAS Build** | **No** | Builds and submits from the cloud; one codebase also ships to Google Play (2× the market) |
| **C. Native Swift + GitHub Actions macOS runner** | Only for first-time setup and testing | Cloud CI builds/uploads on every push (`.github/workflows/ios-testflight.yml`) |

**Path A setup** (on your Mac, in Claude Code):
```
/plugin install xcode@claude-plugins-official
```
Then open the project in Xcode and allow external agents when prompted (Xcode 26.3+).

### 5. Shared web presence (one site, all apps)
Apple requires a **Privacy Policy URL** and a **Support URL** for every app. Make one domain (e.g. `yourstudio.com`) with `/appname/privacy` and `/appname/support` pages, generated from `templates/legal/`. Free hosting: GitHub Pages, Netlify or Vercel.

---

## Part 2 — Per-app pipeline (repeat for each app)

```
scripts/new-app.sh my-app-name      # scaffolds apps/my-app-name/ from templates
```
Then work through `apps/my-app-name/`:

1. **`app-brief.md`**: problem, audience, monetization, competitors. Decide *before* building.
2. **Build** the app (Path A, B or C).
3. **`PrivacyInfo.xcprivacy`**: copy into the Xcode target and edit it to match what the app actually does.
4. **`store-listing.md`**: fill it in, then run `python3 scripts/check-listing.py apps/my-app-name/store-listing.md` to verify Apple's character limits.
5. **Legal pages**: fill in `legal/privacy-policy.md` and `legal/support.md`, then publish them.
6. **Screenshots**: at least the 6.9" iPhone size (1320×2868 portrait). Add 13" iPad if the app supports iPad.
7. **TestFlight**: test on a real device, and ideally with 5–10 outside testers.
8. Go through **`checklists/submission-checklist.md`**, then submit.
9. If rejected, see **`checklists/rejection-playbook.md`**.

---

## Part 3 — Requirements in effect now (verified Nov 2026)
- Uploads must be built with **Xcode 26+ and the iOS 26 SDK** (since Apr 28, 2026).
- Apps must target **iOS 13 or later** (since Sep 9, 2026).
- Third-party SDKs must include a **privacy manifest** and signature. Your manifest, App Privacy labels and actual app behavior must all match.
- Apps that let users create an account must also let them **delete it in-app**.

Recheck developer.apple.com/news/upcoming-requirements before each submission, because these change yearly.

---

## Part 4 — Making it profitable (multi-app strategy)
- **Subscriptions over paid downloads.** Recurring revenue is the passive income you want. Use StoreKit 2 directly or RevenueCat (free until meaningful revenue), which also gives you paywall A/B testing without resubmitting.
- **Shared code, distinct apps.** Reuse your paywall, onboarding, settings and analytics modules across apps, but each app must have a genuinely distinct purpose. Apple's **Guideline 4.3 (spam)** rejects near-duplicate apps from the same account. This is the #1 risk for a multi-app portfolio.
- **Cross-promote.** Add a "More from us" screen in every app. Each new app launches with an audience from the others.
- **App Store Optimization (ASO).** Keywords (100 chars) and subtitle (30 chars) drive search. Don't repeat words already in the app name, because Apple indexes them together.
- **Validate before building.** Put a one-page landing site with an email signup in front of the target audience for about a week. Build only the ideas that get signups.
- **Ship Android too.** Path B (Expo) reaches Google Play ($25 one-time fee) from the same code.
