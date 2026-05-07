# QR / Social / AirDrop / vCard / NFC Architecture

## Data Model Draft

```ts
type Profile = {
  id: string;
  ownerUserId: string;
  displayName: string;
  role: string;
  tagline: string;
  theme: {
    stylePreset: 'neo' | 'clean' | 'retro';
    headlineFont: string;
    bodyFont: string;
    stickers: string[];
    background: string;
  };
  links: SocialLink[];
  contact: PrivateContact;
  visibility: VisibilityPolicy;
  nfcTagIds: string[];
  updatedAt: string;
};

type SocialLink = {
  platform: 'instagram' | 'youtube' | 'threads' | 'x' | 'website';
  handle: string;
  url: string;
  enabled: boolean;
};

type PrivateContact = {
  emailEncrypted?: string;
  phoneEncrypted?: string;
  companyEncrypted?: string;
  vcardEnabled: boolean;
};

type VisibilityPolicy = {
  profile: 'public' | 'token' | 'private';
  contact: 'hidden' | 'afterConsent' | 'public';
  links: 'public' | 'token';
};
```

## QR Flow

1. Published profile gets stable URL: `https://domain.com/p/{profileId}`.
2. QR can optionally include short-lived or revocable token: `/p/{profileId}?t={shareToken}`.
3. QR scan opens profile hub with:
   - card preview
   - Instagram / YouTube / Threads / X buttons
   - save contact button
   - request private contact button if hidden
4. Owner can rotate token without changing profile content. For printed QR, use stable profileId and server-side visibility controls.

## Social Linking

- Normalize platform URLs at input time.
- Store handle and canonical URL separately.
- Validate against allowlisted host patterns:
  - Instagram: `instagram.com/{handle}`
  - YouTube: `youtube.com/@handle`, channel, or custom URL
  - Threads/Meta: `threads.net/@handle`
  - X: `x.com/{handle}`
- Show outbound link confirmation for suspicious or non-canonical URLs.

## AirDrop / vCard

- Web MVP:
  - Generate `.vcf` on demand.
  - Use browser download fallback.
  - Use `navigator.share()` where supported to invoke native share sheet.
- Native iOS future:
  - Create contact card payload and call system share sheet; user can AirDrop contact.
- Privacy rule:
  - vCard includes only fields the owner enabled in publish sheet.

## NFC Physical Card

- NFC tag stores **only redirect URL**, never raw phone/email.
- Recommended payload: `https://domain.com/n/{tagId}` → server resolves to active profile.
- Benefits:
  - Lost card can be disabled.
  - Tag can be reassigned.
  - Owner can change Instagram/YouTube/X/contact without reprinting or rewriting the card.
- Admin/user actions:
  - claim tag
  - link tag to profile
  - update displayed info
  - pause/disable tag
  - view scan analytics with privacy-safe aggregation

## Security / Privacy UX

- Default secure mode ON during input.
- Sensitive fields stored encrypted at rest; public card data stored separately.
- Publish sheet must show exactly what QR/NFC visitors see.
- Contact reveal should be consent-based: visitor requests or taps “save contact,” owner-configured policy decides what appears.
- Analytics should avoid collecting raw contact details or unnecessary visitor identifiers.
