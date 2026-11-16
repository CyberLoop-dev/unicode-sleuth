#!/usr/bin/env python3
"""Find invisible and control Unicode characters in local text files."""
from __future__ import annotations
import argparse, json, sys, unicodedata
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "dist", "build"}
JOINERS = {"\u200c", "\u200d"}

def candidates(root: Path, extensions: set[str] | None):
    paths = [root] if root.is_file() else sorted(root.rglob("*"))
    for path in paths:
        if not path.is_file() or path.is_symlink(): continue
        if any(part in SKIP_DIRS for part in path.parts): continue
        if extensions and path.suffix.lower() not in extensions: continue
        yield path

def scan(path: Path, max_bytes: int, include_joiners: bool):
    try:
        if path.stat().st_size > max_bytes: return []
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError): return []
    findings = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for column, char in enumerate(line, start=1):
            category = unicodedata.category(char)
            if category not in {"Cc", "Cf"}: continue
            if char == "\t" or (char in JOINERS and not include_joiners): continue
            findings.append({"file": str(path), "line": line_no, "column": column,
                "character": repr(char), "codepoint": f"U+{ord(char):04X}",
                "name": unicodedata.name(char, "UNNAMED"), "category": category})
    return findings

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--extensions", help="comma-separated suffixes, e.g. .py,.js,.md")
    parser.add_argument("--max-bytes", type=int, default=2_000_000)
    parser.add_argument("--include-joiners", action="store_true",
                        help="also report zero-width joiners used by some writing systems")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on-findings", action="store_true")
    args = parser.parse_args()
    if not args.path.exists(): parser.error(f"path does not exist: {args.path}")
    extensions = ({x.strip().lower() if x.strip().startswith(".") else "." + x.strip().lower()
                   for x in args.extensions.split(",") if x.strip()} if args.extensions else None)
    findings = []
    for file_path in candidates(args.path, extensions):
        findings.extend(scan(file_path, args.max_bytes, args.include_joiners))
    if args.json: print(json.dumps(findings, indent=2, ensure_ascii=False))
    else:
        for item in findings:
            print(f"{item['file']}:{item['line']}:{item['column']}  {item['codepoint']}  {item['name']}  {item['character']}")
        print(f"\nScanned path: {args.path}\nFindings: {len(findings)}")
    return 1 if findings and args.fail_on_findings else 0

if __name__ == "__main__":
    raise SystemExit(main())
