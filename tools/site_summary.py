import json
import os
from datetime import datetime

# 内置站点资料集合
SITE_PROFILES = [
    {
        "id": "site_001",
        "name": "华体会体育入口",
        "url": "https://main-portal-hth.com.cn",
        "keywords": ["华体会", "体育入口", "主站"],
        "tags": ["体育", "门户"],
        "description": "华体会官方主入口站点，提供全面的体育赛事与娱乐服务。"
    },
    {
        "id": "site_002",
        "name": "华体会资讯中心",
        "url": "https://news-portal-hth.com.cn",
        "keywords": ["华体会", "资讯", "新闻"],
        "tags": ["新闻", "资讯"],
        "description": "华体会旗下资讯平台，聚合每日体育新闻与行业动态。"
    },
    {
        "id": "site_003",
        "name": "华体会社区",
        "url": "https://community-hth.com.cn",
        "keywords": ["华体会", "社区", "论坛"],
        "tags": ["社区", "互动"],
        "description": "华体会用户交流社区，分享赛事讨论与活动信息。"
    }
]

def load_site_data() -> list:
    """加载并返回站点资料列表，可扩展支持外部文件读取"""
    return SITE_PROFILES

def build_summary(site: dict) -> str:
    """为单个站点构建结构化摘要文本"""
    lines = []
    lines.append(f"站点名称：{site['name']}")
    lines.append(f"访问地址：{site['url']}")
    lines.append(f"关键词：{', '.join(site['keywords'])}")
    lines.append(f"标签：{' / '.join(site['tags'])}")
    lines.append(f"说明：{site['description']}")
    return "\n".join(lines)

def generate_all_summaries(sites: list) -> list:
    """生成所有站点的摘要"""
    summaries = []
    for idx, site in enumerate(sites, start=1):
        header = f"--- 站点 {idx} ---"
        summary = build_summary(site)
        full = f"{header}\n{summary}"
        summaries.append(full)
    return summaries

def archive_summaries(summaries: list, output_dir: str = "output"):
    """将摘要归档到指定目录，可选写入文件"""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"site_summary_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    content = "\n\n".join(summaries)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

def print_full_report(sites: list):
    """打印完整摘要报告到控制台"""
    print("=" * 48)
    print("  内置站点资料 — 结构化摘要报告")
    print("=" * 48)
    for idx, site in enumerate(sites, start=1):
        print(f"\n站点 {idx}: {site['name']}")
        print("-" * 40)
        print(f"  URL       : {site['url']}")
        print(f"  关键词    : {', '.join(site['keywords'])}")
        print(f"  标签      : {' / '.join(site['tags'])}")
        print(f"  说明      : {site['description']}")
    print("\n" + "=" * 48)

def main():
    sites = load_site_data()
    summaries = generate_all_summaries(sites)
    print_full_report(sites)
    filepath = archive_summaries(summaries)
    print(f"摘要已写入文件：{filepath}")

if __name__ == "__main__":
    main()