---
name: web-accessibility-audit
description: >-
  Audits web applications for Web Content Accessibility Guidelines (WCAG 2.1 AA) compliance.
  Checks color contrast ratios, missing form labels, button accessible names,
  heading hierarchy levels, and keyboard accessibility.
---

# Web Accessibility Audit Skill (`web-accessibility-audit`)

This skill audits HTML/CSS web applications against the **Web Content Accessibility Guidelines (WCAG 2.1 Level AA)** to ensure usability for citizens with visual, auditory, motor, or cognitive impairments.

## Core Accessibility Checkpoints

### 1. Form Field Labels (WCAG 1.3.1, 4.1.2)
- Every `<input>`, `<textarea>`, and `<select>` must have an associated `<label for="id">` or an explicit `aria-label` / `aria-labelledby` attribute.
- Placeholder text is not a replacement for a permanent label.

### 2. Button & Interactive Element Accessible Names (WCAG 4.1.2)
- Icon-only buttons (e.g. `<button><i data-lucide="menu"></i></button>`) must include `aria-label="เมนูหลัก"` or a `title` attribute so screen readers announce their function.

### 3. Heading Hierarchy (WCAG 1.3.1)
- Headings should follow a logical outline: `<h1>` -> `<h2>` -> `<h3>` without skipping levels (e.g. going straight from `<h1>` to `<h4>`).

### 4. Text Contrast Ratios (WCAG 1.4.3)
- Normal body text must achieve a contrast ratio of at least **4.5:1** against its background.
- Large text (18pt+ or 14pt bold+) must achieve at least **3.0:1**.
- Common pitfalls: Light amber text on white background (e.g. `text-amber-400` on `bg-white`), or light grey text on white (e.g. `text-slate-400` on `bg-slate-50`).

### 5. Keyboard Navigation & Focus Visible (WCAG 2.4.7)
- All interactive controls must receive keyboard focus via `Tab` and show a visible focus outline (`focus:ring-2` or `focus:outline-indigo-500`).

## Automated Accessibility Script
Run the automated a11y checker:
```bash
python3 .agents/skills/web-accessibility-audit/scripts/audit_a11y.py <path-to-html-file>
```
