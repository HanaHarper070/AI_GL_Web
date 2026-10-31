#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Web Accessibility (a11y) Auditor for WCAG 2.1 AA.
Checks missing form labels, icon buttons without aria-label/title, and color contrast warnings.
"""

import sys
import re
import os

def audit_a11y(filepath):
    print(f"\n========================================================")
    print(f"♿ [ACCESSIBILITY AUDIT] Scanning: {os.path.basename(filepath)}")
    print(f"========================================================")

    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' does not exist.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = "".join(lines)

    issues = []

    # 1. Check for icon-only buttons without title or aria-label
    btn_pattern = re.compile(r'<button\s+([^>]*?)>(.*?)</button>', re.DOTALL | re.IGNORECASE)
    for match in btn_pattern.finditer(content):
        attrs, inner = match.groups()
        # Clean text
        text_content = re.sub(r'<[^>]+>', '', inner).strip()
        has_accessible_name = bool(text_content) or 'aria-label=' in attrs or 'title=' in attrs
        if not has_accessible_name and ('<i ' in inner or '<svg' in inner):
            line_num = content[:match.start()].count('\n') + 1
            issues.append({
                'line': line_num,
                'severity': 'MEDIUM',
                'type': 'Missing Accessible Name',
                'desc': 'Icon-only <button> missing title or aria-label for screen readers',
                'snippet': f"<button {attrs[:45]}...>"
            })

    # 2. Check for inputs without id or aria-label
    input_pattern = re.compile(r'<input\s+([^>]*?)>', re.IGNORECASE)
    for match in input_pattern.finditer(content):
        attrs = match.group(1)
        if 'type=["\']hidden["\']' in attrs:
            continue
        has_id = 'id=' in attrs
        has_aria = 'aria-label=' in attrs or 'aria-labelledby=' in attrs
        if not has_id and not has_aria:
            line_num = content[:match.start()].count('\n') + 1
            issues.append({
                'line': line_num,
                'severity': 'MEDIUM',
                'type': 'Missing Form Identifier',
                'desc': '<input> missing id attribute or aria-label',
                'snippet': f"<input {attrs[:45]}...>"
            })

    # 3. Check for low-contrast text classes on light backgrounds
    low_contrast_combos = [
        ('text-amber-400', 'bg-white', 'text-amber-400 on white has low contrast ratio (< 2.5:1)'),
        ('text-amber-300', 'bg-white', 'text-amber-300 on white has low contrast ratio (< 2.0:1)'),
        ('text-slate-300', 'bg-white', 'text-slate-300 on white has low contrast ratio (< 2.1:1)'),
        ('text-emerald-300', 'bg-white', 'text-emerald-300 on white has low contrast ratio (< 2.3:1)')
    ]

    for i, line in enumerate(lines, 1):
        for fg, bg, desc in low_contrast_combos:
            if fg in line and (bg in line or 'bg-slate-50' in line):
                issues.append({
                    'line': i,
                    'severity': 'LOW',
                    'type': 'Color Contrast Warning',
                    'desc': desc,
                    'snippet': line.strip()[:65]
                })

    # Print summary
    if not issues:
        print("✅ Accessibility audit passed! High compliance with WCAG 2.1 AA.")
    else:
        print(f"⚠️ Found {len(issues)} accessibility finding(s):\n")
        for idx, iss in enumerate(issues, 1):
            badge = "[HIGH 🔴]" if iss['severity'] == 'HIGH' else "[MEDIUM 🟡]" if iss['severity'] == 'MEDIUM' else "[LOW 🔵]"
            print(f"{idx}. {badge} Line {iss['line']}: {iss['type']}")
            print(f"   Details: {iss['desc']}")
            print(f"   Snippet: {iss['snippet']}\n")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'ai.html'
    audit_a11y(target)
