---
name: web-qa-tester
description: >-
  Automated Quality Assurance (QA) and error testing skill for web applications.
  Verifies internal link targets, element ID existence, onclick handler existence,
  unclosed HTML tags, and JavaScript runtime edge-case exceptions.
---

# Web QA Tester Skill (`web-qa-tester`)

This skill performs rigorous functional quality assurance (QA) on HTML/JS web applications to catch broken features, missing IDs, unhandled edge cases, and runtime exceptions before release.

## Core QA Test Categories

### 1. Element ID & Navigation Reference Integrity
- Every `document.getElementById('xyz')` must have a corresponding `<... id="xyz">` in the DOM.
- Every tab switcher or view switcher function (e.g. `switchMainView('xyz')`) must have a corresponding view element (`view-xyz`) and navigation button (`nav-btn-xyz`).

### 2. Onclick Handler & Function Binding Integrity
- Every inline `onclick="foo()"` must have a corresponding JavaScript function definition `function foo(...)` in the script scope.
- Catches typos in function names or deleted functions that cause silent button clicks.

### 3. Edge-Case Input & Empty State Validation
- Form fields submitted while completely blank or whitespace-only must not cause exceptions or blank cards.
- Reset buttons must clear all related states and restore default placeholders.
- When an array (e.g. saved prompts, module list) is empty, a clean, friendly empty state must be displayed rather than a broken or blank box.

### 4. HTML Well-Formedness
- Validates that all opening tags (except standard void elements) have matching closing tags in the proper nesting order.

## Automated QA Script
Run the automated QA test suite:
```bash
python3 .agents/skills/web-qa-tester/scripts/audit_qa.py <path-to-html-file>
```
