# Rejection Playbook

Rejections are normal, especially for a first app. Most are fixed in a day.

## How to respond
1. Read the rejection in App Store Connect → Resolution Center. Note the **guideline number**.
2. If it's a misunderstanding, **reply in Resolution Center** with a clear explanation and screenshots/video. No new build is needed.
3. If it's a real issue, fix it, increment the build number, upload, and reply describing the fix.
4. If you believe the decision is wrong after replying, file an appeal with the App Review Board.

## Most common rejections and fixes
| Guideline | What it means | Fix |
|---|---|---|
| **2.1** App Completeness | Crash, bug, or reviewer couldn't log in | Fix the crash; add a working demo account in Review Notes |
| **2.3** Accurate Metadata | Screenshots or description don't match the app | Use real screenshots; remove claims about features you don't have |
| **3.1.1** In-App Purchase | Digital content unlocked without IAP | Route digital purchases through IAP |
| **3.1.2** Subscriptions | Paywall missing terms, price or restore | Add price/period, Terms + Privacy links, Restore button |
| **4.2** Minimum Functionality | Too simple, or a website wrapped in an app | Add native features (widgets, offline mode, notifications) |
| **4.3** Spam | Too similar to another app (including your own) | Make each app distinct in purpose, UI and features; don't clone templates with new skins |
| **5.1.1** Data Collection | Unneeded permissions, vague usage strings, no account deletion | Ask only when needed; write specific strings; add in-app deletion |
| **5.1.2** Data Use | Privacy labels don't match behavior | Make the labels, manifest and code agree |

## Multi-app warning
If one account gets several 4.3 rejections, Apple may flag the whole developer account. Space out launches and make sure every app passes the "would someone pay for this on its own?" test.
