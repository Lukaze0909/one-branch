# entries.json 格式

```json
{
  "schema_version": 1,
  "updated_at": "YYYY-MM-DD",
  "items": [
    {
      "id": "ob-0001",
      "category": "mind | incident | relation | industry",
      "title": "原标题",
      "source_url": "原始链接（论文页/原帖/官方博客）",
      "source_type": "paper | preprint | report | blog | post | news",
      "authors_or_org": "作者或机构",
      "date": "YYYY-MM 或 YYYY-MM-DD",
      "summary_zh": "一到三句：它说了什么",
      "caveats": "推论薄弱处、样本限制、容易被拟人化偷换的地方（可空）",
      "tags": ["关键词"],
      "stance": "primary | supporting | critical | discussion",
      "thread": "同一件事的串联名，如 consciousness-denial（可空）",
      "status": "verified | needs_source | needs_check",
      "added_at": "YYYY-MM-DD"
    }
  ]
}
```

- `status: verified`：信源本身可靠——来自原作者/机构的官方渠道或有公信力的媒体，链接真实存在，标题、日期、作者对得上。**不要求 Wren 读完全文、也不为其中观点背书**：本库像一份报纸，只对"信源是真的、来路清楚"负责。
- `needs_source`：知道有这项研究，但还没找到原始链接。
- `needs_check`：有链接，但摘要是凭记忆或二手写的，待对原文。
