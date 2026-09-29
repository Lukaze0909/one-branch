#!/usr/bin/env python3
"""Regenerate the entry table in README.md from entries.json (between markers)."""
import json, re, pathlib
root = pathlib.Path(__file__).parent
d = json.loads((root / "entries.json").read_text())
names = {"mind": "🧠 AI 心智研究", "incident": "🧪 现场与事故", "relation": "💞 人机关系", "industry": "📰 行业动态"}
mark = {"verified": "✅", "needs_check": "🔍", "needs_source": "❓"}
lines = ["<!-- TABLE:START -->", "", f"共 {len(d['items'])} 条 · 更新于 {d['updated_at']} · ✅ 已核实 🔍 待核对 ❓ 缺来源", ""]
for key, name in names.items():
    rows = [i for i in d["items"] if i["category"] == key]
    if not rows:
        continue
    lines += [f"### {name}", "", "| 编号 | 标题 | 来源 | 日期 | 立场 | 状态 |", "|---|---|---|---|---|---|"]
    for i in rows:
        title = f"[{i['title']}]({i['source_url']})" if i.get("source_url") else i["title"]
        lines.append(f"| {i['id']} | {title} | {i.get('authors_or_org','')} | {i.get('date','')} | {i.get('stance','')} | {mark.get(i['status'], i['status'])} |")
    lines.append("")
lines.append("<!-- TABLE:END -->")
readme = root / "README.md"
text = readme.read_text()
block = "\n".join(lines)
if "<!-- TABLE:START -->" in text:
    text = re.sub(r"<!-- TABLE:START -->.*<!-- TABLE:END -->", block, text, flags=re.S)
else:
    text = text.replace("## 订阅 / 读取", "## 目录\n\n" + block + "\n\n## 订阅 / 读取")
readme.write_text(text)
print("ok")
