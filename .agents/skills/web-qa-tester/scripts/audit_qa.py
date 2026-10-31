#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Functional QA & Integrity Tester for HTML/JS applications.
Scans for missing getElementById references, undefined onclick handlers, and broken views.
"""

import sys
import re
import os
from html.parser import HTMLParser

class TagNestingValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_elements:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_elements:
            return
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (from line {pos[0]}), found </{tag}> at line {self.getpos()[0]}")

def test_file(filepath):
    print(f"\n========================================================")
    print(f"🧪 [QA TEST SUITE] Testing: {os.path.basename(filepath)}")
    print(f"========================================================")

    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' does not exist.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # 1. HTML Syntax & Nesting Check
    validator = TagNestingValidator()
    validator.feed(content)
    if validator.errors:
        for err in validator.errors[:5]:
            issues.append({'severity': 'HIGH', 'type': 'HTML Nesting Error', 'desc': err})
    if validator.stack:
        for tag, pos in validator.stack[-5:]:
            issues.append({'severity': 'HIGH', 'type': 'Unclosed Tag', 'desc': f"Unclosed <{tag}> from line {pos[0]}"})

    # 2. Extract all defined element IDs
    defined_ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))

    # 3. Check getElementById calls
    get_elem_calls = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', content)
    missing_ids = set()
    for el_id in get_elem_calls:
        # Ignore dynamic template IDs (e.g. quiz-exp-${qIdx})
        if '$' in el_id or '{' in el_id:
            continue
        if el_id not in defined_ids:
            missing_ids.add(el_id)

    for m_id in sorted(missing_ids):
        issues.append({
            'severity': 'HIGH',
            'type': 'Missing DOM Element ID',
            'desc': f"getElementById('{m_id}') called in JS, but <... id='{m_id}'> does not exist in HTML!"
        })

    # 4. Extract all defined JS functions (inline + referenced external scripts)
    defined_funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', content))
    var_funcs = set(re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:\([^)]*\)|[a-zA-Z0-9_]+)\s*=>', content))
    all_funcs = defined_funcs | var_funcs

    # Also load local external script tags
    dir_path = os.path.dirname(filepath) or '.'
    ext_scripts = re.findall(r'<script\s+[^>]*src=["\']([^"\']+\.js)["\']', content)
    for s_file in ext_scripts:
        if s_file.startswith('http') or s_file.startswith('//'):
            continue
        s_path = os.path.join(dir_path, s_file)
        if os.path.exists(s_path):
            with open(s_path, 'r', encoding='utf-8') as sf:
                s_code = sf.read()
                all_funcs |= set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', s_code))
                all_funcs |= set(re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:\([^)]*\)|[a-zA-Z0-9_]+)\s*=>', s_code))

    # 5. Check inline onclick function calls
    onclick_calls = re.findall(r'onclick=["\']([a-zA-Z0-9_]+)\(', content)
    for fn in set(onclick_calls):
        # Ignore native or window methods
        if fn in {'event', 'alert', 'confirm', 'prompt', 'print', 'close', 'focus', 'blur'}:
            continue
        if fn not in all_funcs:
            issues.append({
                'severity': 'HIGH',
                'type': 'Undefined Function in Onclick',
                'desc': f"Button calls onclick='{fn}()', but function '{fn}' is not defined in <script>!"
            })

    # Print summary
    if not issues:
        print(f"✅ All QA checks passed! (Total IDs checked: {len(defined_ids)}, Functions: {len(all_funcs)})")
    else:
        print(f"⚠️ Found {len(issues)} functional QA issue(s):\n")
        for idx, iss in enumerate(issues, 1):
            badge = "[HIGH 🔴]" if iss['severity'] == 'HIGH' else "[MEDIUM 🟡]"
            print(f"{idx}. {badge} {iss['type']}: {iss['desc']}")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'ai.html'
    test_file(target)
