# Privacy Policy

MemoryFit (FSRS-based memory training app)

Last updated: September 27, 2026

## 1. Information We Collect

- Device or app identifiers, such as an app installation identifier used for error reporting. On iOS, RevenueCat processes the identifier for vendor (IDFV).

- Account information, such as email address and login provider identifier, when you sign in.

- Study data, including decks, card content, review records, and learning statistics.

- Contacts information, such as names and phone numbers, only when you choose to create a contacts deck.

- Camera images or user-selected images, only when you choose to create image cards.

- Voice input, only when you use spoken answer features. The device's speech recognition service processes speech and may use the network depending on the device and its settings.

- For AI features: content you enter or import, text extracted from PDFs, web pages, or videos, generation options, image prompts, and technical logs needed to process requests.

- Purchase and credit usage records, such as product IDs, transaction identifiers, and credit usage history.

- Crash and diagnostic information, such as error details and time, app version, device model, and operating system. App versions with error reporting enabled may send this information to Sentry.

- Usage analytics: an account identifier (including an automatically created anonymous account), event types for app opens, deep links, deck installation or publication, sharing, review prompt display, and study session starts, completions, or explicit abandonment; identifiers for study sessions, decks, shared decks, and templates; card counts; study scope, installation source, deck category, and publication credit price; device event time and server receipt time. Analytics events do not include card front or back content.

## 2. How We Use Information

- To provide optimized spaced repetition scheduling using an FSRS-style workflow.

- To store and sync decks, cards, review records, and learning progress.

- To provide AI card generation and AI image generation.

- To create learning cards from contacts when you choose that feature.

- To provide learning statistics and progress tracking.

- To process credit purchases, credit usage, refunds, and abuse prevention.

- To improve app functionality, analyze errors, maintain security, and prevent misuse.

- To improve app stability using crash and diagnostic information.

- To analyze app usage and the flow of study session starts, completions, and explicit abandonment linked to an account identifier. A start without an outcome event does not by itself prove that a user abandoned the session.

Usage analytics events are temporarily stored on your device when an account identifier is available. The app may create an anonymous account even if you do not sign in with email or a social provider, so analytics events may be linked to that account. Events recorded without an account identifier are not saved, and events saved for one account are not assigned to a later account. The app attempts to send events to Supabase in a batch when a certain number have accumulated or the app moves to the background. Failed transfers are retried. When the device storage limit is reached, the oldest records are removed first.

## 3. AI Features and Third-Party AI Processing

- MemoryFit uses AI processing only when you choose AI card generation or AI image generation.

- Purpose: automatic study card generation, educational image generation, request processing, and credit usage management.

- Data sent: content you enter or import, extracted text from PDFs, web pages, or videos, generation options such as language, difficulty, or card type, AI image prompts, and technical logs needed to process requests.

- Processing route: AI requests are processed through MemoryFit servers using Supabase Edge Functions.

- Third-party AI provider: Google Gemini API.

- When data is sent: when you start AI card generation or AI image generation.

- What is not sent: existing local decks and cards are not sent to the third-party AI provider unless you choose to use AI generation.

- Retention and logs: AI request data is processed to provide the feature and may be retained in service logs under relevant provider terms and policies for security, abuse prevention, operations, and legal obligations.

- In-app path: Settings > AI Settings > AI Data Use.

## 4. Retention

- Study data: retained until app deletion, account deletion, or your deletion request.

- Contacts information: processed on device and not sent to MemoryFit servers.

- Camera images: processed for the selected feature and not sent to Google Gemini API unless you separately enter or send them through an AI feature.

- Spoken answers: the device's speech recognition service converts speech to text and may transmit audio off the device depending on its settings. MemoryFit servers do not receive the audio recording itself. Retention by the recognition provider follows that provider's policies.

- AI request data: processed to provide the feature and may be retained in service logs under relevant provider terms and policies for security, abuse prevention, operations, and legal obligations.

- Purchase and credit records: may be retained as needed for transaction verification, refunds, accounting, and dispute handling.

- Device or app identifiers and crash or diagnostic information: may be processed as needed to provide features and analyze errors. Retention by external services follows their policies; we do not promise a fixed retention period.

- Usage analytics: events stored on the server have no configured fixed retention period or automatic expiration. When you delete your account, the link between the events and your account identifier is removed, but event types, additional information, and timestamps remain. Unsent analytics records temporarily stored on your device are also not separately removed by the account deletion process. You can request deletion of analytics information using the contact details below.

## 5. Third-Party Sharing

- Google Gemini API, when you use AI card generation or AI image generation.  

Data shared: user-entered or imported study content, extracted text from PDFs, web pages, or videos, generation options, image prompts, and technical logs needed to process requests.  

Purpose: automatic study card generation and educational image generation.

- Google Play Billing / Apple In-App Purchase / RevenueCat, when processing and validating credit purchases.  

Data shared: purchased product ID, transaction identifier, app user identifier, and information needed for purchase validation. On iOS, RevenueCat requests include the identifier for vendor (IDFV) and app user identifier.  

Purpose: payment processing, purchase restoration, credit fulfillment, and refund handling.

Except as described above or as required by law, MemoryFit does not provide personal information to third parties.

## 6. Service Providers and International Processing

- Supabase Inc. (United States): database hosting, authentication, server-side functions, and storage and processing of usage analytics events linked to an account identifier.  

Contact: [supabase.com/contact](https://supabase.com/contact)

- RevenueCat: processes purchase and subscription status, purchase validation, and restoration, including purchase history, transaction information, and app user identifiers. On iOS, purchase-related requests transmit the identifier for vendor (IDFV) alongside the app user identifier.

- Sentry: in app versions with error reporting enabled, processes an app installation identifier, crash and error logs, and app or device diagnostic information. Filters are applied to reduce transmission of sensitive content such as card text. Processing of connection IP addresses may depend on service settings.

- Device speech recognition provider: converts speech to text when you choose a spoken answer. The provider varies by device and operating system settings and may process speech over the network.

- Google Gemini API / Google LLC or related Google affiliates: AI request processing.  

Data processed: AI feature content, generation options, image prompts, and technical logs.  

Related policy: [Gemini API Data Logging and Sharing](https://ai.google.dev/gemini-api/docs/logs-policy)

## 7. Contacts Access

- MemoryFit can read names and phone numbers from contacts to create learning cards when you choose that feature.

- Contacts information is processed on device and is not sent to MemoryFit servers.

- Contacts access is optional. You can use the app without granting this permission.

## 8. Camera and Microphone

- Camera: used to create image cards.

- Microphone: used for spoken answers and text-to-speech related features.

- Captured images are not sent to Google Gemini API unless you separately enter or send them through an AI feature. Spoken answers are processed by the device's speech recognition service, which may send audio over the network depending on the device and settings.

## 9. Offline Use

MemoryFit supports offline study. AI generation, backup, purchase validation, and speech recognition on some devices or settings may require a network connection.

Usage analytics events recorded while offline may remain temporarily on your device and be sent after connectivity returns.

## 10. Your Rights and Account Deletion

To request deletion of your MemoryFit account in the app, open Settings, select “Delete account,” and confirm. Anonymous accounts can also be deleted in the app. Analytics records described in section 4 and records held by external payment providers may remain after account deletion.

If you cannot use the app or prefer to request deletion outside the app, email [mkideabox@gmail.com](mailto:mkideabox@gmail.com?subject=MemoryFit%20account%20deletion) with the subject “MemoryFit account deletion.” Include your sign-in email or information that lets us identify your account. We will verify your identity before processing the request. Do not send passwords or verification codes.

### Request data deletion while keeping your account

You may request access, correction, deletion, restriction of processing, or withdrawal of consent without deleting your entire account. Email [mkideabox@gmail.com](mailto:mkideabox@gmail.com?subject=MemoryFit%20data%20deletion) with the subject “MemoryFit data deletion,” the data you want deleted, and information that lets us identify your account. This also applies to usage analytics deletion requests. See section 4 for retention details and records that may remain after account deletion.

## 11. Security

MemoryFit applies reasonable technical and organizational safeguards, including HTTPS for communication with MemoryFit servers, Supabase Row Level Security, authentication-based access controls, and device storage protection. Network processing by the device speech recognition service depends on its provider and device settings.

## 12. Privacy Officer

Privacy Officer: hyung-woo park

Email: mkideabox@gmail.com

Phone: +82-10-4732-7825

## 13. Changes

- September 27, 2026: Added details about account-linked usage analytics, including anonymous accounts, batch transfer, retention, and records that may remain after account deletion.

- May 6, 2026: Added details about AI features, third-party AI processing, credit purchase processing, retention, and logs.
