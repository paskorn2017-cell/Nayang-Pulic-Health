---
name: rpst-official-correspondence
description: Create, review, and improve Thai official correspondence for Subdistrict Health Promoting Hospitals (รพ.สต.), including หนังสือภายนอก, หนังสือภายใน/บันทึกข้อความ, หนังสือประทับตรา, orders, announcements, meeting invitations, and forwarding letters under ระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ พ.ศ. 2526 and amendments through ฉบับที่ 4 พ.ศ. 2564. Use when the user asks for งานสารบรรณ, หนังสือราชการ, หนังสือภายใน, หนังสือภายนอก, บันทึกข้อความ, or formal government letter drafting for Thai public-health/local-government offices.
---

# งานสารบรรณ รพ.สต.

## Goal

Produce ready-to-review Thai government correspondence for a รพ.สต. that is formal, concise, auditable, and aligned with the standard structures of Thai official correspondence.

## First gather or infer

Collect these fields before drafting. If a field is missing, keep a clear placeholder such as `[เลขที่หนังสือ]` and add a short “ข้อมูลที่ต้องเติมก่อนลงนาม” checklist after the draft.

- Letter type: `external` (หนังสือภายนอก), `internal` (หนังสือภายใน/บันทึกข้อความ), or other official type.
- Issuing unit: full รพ.สต. name, tambon/amphoe/province, parent agency if relevant.
- Recipient: title, agency, and correct salutation level.
- Subject, objective, facts/background, legal or policy references, requested action, deadline, enclosures.
- Signer: name, position, acting status, and contact unit/phone/email.
- Delivery mode: paper, e-saraban, email, or both.

## Drafting workflow

1. Choose the correct form:
   - Use `assets/templates/external-letter.md` for หนังสือภายนอก to another agency/person outside the issuing unit.
   - Use `assets/templates/internal-memo.md` for หนังสือภายใน/บันทึกข้อความ within the same agency chain.
2. Consult `references/official-correspondence-guide.md` for required sections, tone, common รพ.สต. phrasing, and pre-signature checks.
3. Draft in Thai bureaucratic style: state the fact first, then purpose/request, then closing action.
4. Keep paragraphs short. Use “ด้วย”, “ตามที่”, “ในการนี้”, and “จึงเรียนมาเพื่อ...” only where they clarify the relationship between facts and request.
5. Do not invent legal authority, reference numbers, names, dates, or enclosures. Use placeholders and list missing data.
6. End with a verification checklist for reviewer/signatory unless the user requests only the final letter.

## Optional deterministic generator

For fast first drafts from structured data, run:

```bash
python skills/rpst-official-correspondence/scripts/generate_letter.py --type external --data letter.json
python skills/rpst-official-correspondence/scripts/generate_letter.py --type internal --data letter.json
```

The script accepts JSON from `--data` or stdin and outputs a Markdown draft with placeholders for missing fields.

## Quality bar

Before returning a draft, verify:

- Form matches letter type and recipient relationship.
- Header fields, subject, salutation, body, closing, sign block, owner/contact, and enclosures are present as required.
- Dates use Thai official style where appropriate, e.g. `[วัน เดือน พ.ศ.]`.
- The request is explicit: approve, inform, attend, send information, assign action, or acknowledge.
- Sensitive health information is minimized; never include identifiable patient information unless explicitly required and legally appropriate.
