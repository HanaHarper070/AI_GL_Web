---
name: web-security-audit
description: >-
  Audits web applications for security vulnerabilities, OWASP Top 10 client-side risks,
  DOM-based Cross-Site Scripting (XSS), LocalStorage tampering, PDPA personal data leakage,
  and reverse tabnabbing. Use whenever creating, testing, or reviewing web applications.
---

# Web Security & Vulnerability Audit Skill (`web-security-audit`)

This skill inspects and hardens client-side web applications against common security vulnerabilities, data leaks, and code injection attacks.

## Core Audit Checkpoints

### 1. DOM-Based Cross-Site Scripting (XSS)
- **Risk:** Directly inserting dynamic user input or untrusted state into `element.innerHTML`, `element.outerHTML`, or `document.write()` without HTML escaping or sanitization.
- **Rule:** 
  - Never do `element.innerHTML = \`<div>${userInput}</div>\`` without escaping characters: `&`, `<`, `>`, `"`, `'`.
  - Always use `element.textContent` for plain text, or pass dynamic text through a strict `escapeHtml(str)` helper:
    ```javascript
    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }
    ```

### 2. Reverse Tabnabbing & External Links
- **Risk:** Links with `target="_blank"` without `rel="noopener noreferrer"` allow the opened page to access `window.opener.location`, potentially redirecting the user to a malicious phishing site.
- **Rule:** Every `<a target="_blank">` MUST include `rel="noopener noreferrer"`.

### 3. LocalStorage Poisoning & JSON Schema Validation
- **Risk:** Parsing unvalidated or corrupted data from `localStorage` using `JSON.parse()` can crash the application or inject rogue objects.
- **Rule:** Wrap all `JSON.parse(localStorage.getItem(...))` in `try...catch` blocks and validate object keys/types before assigning to application state.

### 4. PDPA & Sensitive Data Protection
- **Risk:** Exposing 13-digit Thai National ID numbers, telephone numbers, or citizen records in unmasked form, query strings, or error alerts.
- **Rule:** Implement automatic regex masking or alert warnings (`/\b\d{13}\b/`) before storing or rendering sensitive context.

### 5. URI Decoding Failures
- **Risk:** Calling `decodeURIComponent(str)` on malformed percent-encoded sequences throws an uncaught `URIError` and breaks the UI.
- **Rule:** Wrap all `decodeURIComponent` in `try...catch` with a fallback to the raw string.

## Automated Audit Script
Run the built-in security auditor:
```bash
python3 .agents/skills/web-security-audit/scripts/audit_security.py <path-to-html-file>
```
