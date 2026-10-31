#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Web Security Auditor for HTML/JS applications.
Scans for DOM-XSS, Missing rel="noopener noreferrer", unhandled URI decoding, and unsafe storage access.
"""

import sys
import re
import os

def audit_file(filepath):
    print(f"\n========================================================")
    print(f"🔒 [SECURITY AUDIT] Scanning: {os.path.basename(filepath)}")
    print(f"========================================================")

    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' does not exist.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    issues = []

    # 1. Check target="_blank" without rel="noopener" or rel="noreferrer"
    blank_pattern = re.compile(r'<a\s+[^>]*target=["\']_blank["\'][^>]*>', re.IGNORECASE)
    for i, line in enumerate(lines, 1):
        for match in blank_pattern.finditer(line):
            tag = match.group(0)
            if 'rel=' not in tag or ('noopener' not in tag and 'noreferrer' not in tag):
                issues.append({
                    'line': i,
                    'severity': 'MEDIUM',
                    'type': 'Reverse Tabnabbing',
                    'desc': 'Found <a target="_blank"> missing rel="noopener noreferrer"',
                    'snippet': tag[:70]
                })

    # 2. Check for dangerous innerHTML usage with unescaped template variables
    inner_html_pattern = re.compile(r'\.innerHTML\s*=\s*`([^`]*)`', re.DOTALL)
    for match in inner_html_pattern.finditer(content):
        matched_str = match.group(0)
        start_pos = match.start()
        line_num = content[:start_pos].count('\n') + 1
        
        # Look for raw template variables like ${item.xxx} without escapeHtml
        raw_vars = re.findall(r'\$\{(?!escapeHtml|idx|i\b|index)[^}]+\}', matched_str)
        if raw_vars:
            suspicious = [v for v in raw_vars if any(keyword in v for keyword in ['role', 'task', 'context', 'format', 'title', 'name', 'desc', 'content', 'input', 'val', 'user'])]
            if suspicious:
                issues.append({
                    'line': line_num,
                    'severity': 'HIGH',
                    'type': 'DOM-based XSS Risk',
                    'desc': f'Unescaped variable inside innerHTML template: {", ".join(suspicious[:3])}',
                    'snippet': matched_str.splitlines()[0][:70] + '...'
                })

    # 3. Check for unhandled decodeURIComponent
    for i, line in enumerate(lines, 1):
        if 'decodeURIComponent(' in line:
            # Check if try is within 3 lines before
            surrounding = " ".join(lines[max(0, i-4):i+2])
            if 'try' not in surrounding or 'catch' not in surrounding:
                issues.append({
                    'line': i,
                    'severity': 'LOW',
                    'type': 'Unhandled URIError',
                    'desc': 'decodeURIComponent() called outside try-catch block',
                    'snippet': line.strip()[:70]
                })

    # 4. Check for unvalidated JSON.parse(localStorage)
    for i, line in enumerate(lines, 1):
        if 'JSON.parse(' in line and 'localStorage' in line and 'try' not in line:
            issues.append({
                'line': i,
                'severity': 'MEDIUM',
                'type': 'LocalStorage Crash Risk',
                'desc': 'JSON.parse(localStorage) without immediate try-catch wrapper',
                'snippet': line.strip()[:70]
            })

    # Report results
    if not issues:
        print("✅ No critical security issues found! Safe clean baseline.")
    else:
        print(f"⚠️ Found {len(issues)} security finding(s):\n")
        for idx, iss in enumerate(issues, 1):
            badge = "[HIGH 🔴]" if iss['severity'] == 'HIGH' else "[MEDIUM 🟡]" if iss['severity'] == 'MEDIUM' else "[LOW 🔵]"
            print(f"{idx}. {badge} Line {iss['line']}: {iss['type']}")
            print(f"   Details: {iss['desc']}")
            print(f"   Snippet: {iss['snippet']}\n")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'ai.html'
    audit_file(target)
