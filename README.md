<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=160&section=header&text=Unicode%20Sleuth&fontSize=38&fontColor=ffffff" width="100%" alt="Unicode Sleuth banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=0F766E&center=true&vCenter=true&width=820&lines=Spot+hidden+Unicode+characters+in+source+text" alt="Animated project title" />
<p>Find invisible and directional Unicode control characters in text files, with code-point reports and read-only scanning.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/unicode-sleuth?style=for-the-badge" alt="MIT license" /> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/unicode-sleuth?style=for-the-badge" alt="Top language" /> <img src="https://img.shields.io/github/stars/CyberLoop-dev/unicode-sleuth?style=for-the-badge" alt="Stars" /> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/unicode-sleuth?style=for-the-badge" alt="Last commit" /></p>
<img src="assets/illustration.svg" width="92%" alt="Unicode inspection illustration" /></div>

## 🎯 Overview

Unicode Sleuth scans text files for control and formatting characters that can make text look different from how it is stored. It reports file, line, column, code point, and Unicode name. The scanner is read-only and skips common generated folders.

## ✨ Features

- 🔍 Detects invisible formatting and control characters.
- ↔️ Highlights bidirectional text controls and zero-width characters.
- 🧭 Shows exact Unicode code points and character names.
- 📄 Supports plain-text and JSON output.
- 🛡️ Never edits or deletes scanned files; joiners used in many languages are excluded by default.

## 🎬 Demo

<pre><code>python main.py . --extensions .py,.js,.ts,.md
python main.py examples/sample.txt --json</code></pre>

## 🚀 Quick Start

<pre><code>python main.py . --extensions .py,.js,.ts,.md</code></pre>

## 🧰 Tech Stack

- Python 3.10+ standard library
- unicodedata, pathlib, and argparse

## 🗂️ Folder Structure

<pre><code>unicode-sleuth/
├── main.py
├── requirements.txt
├── examples/
│   └── sample.txt
└── assets/
    └── illustration.svg</code></pre>

## 🧭 Roadmap

- [ ] Add an optional allow-list for known formatting characters.
- [ ] Add SARIF output for code-scanning workflows.
- [ ] Add a baseline file to suppress reviewed findings.

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, explain behavior changes, and include a reproducible example for bug reports.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer" /></div>
