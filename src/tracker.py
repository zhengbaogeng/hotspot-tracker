#!/usr/bin/env python3
"""
Hotspot Tracker - 热点追踪工具
自动抓取微博热搜、知乎热榜、头条热文
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

# 数据存储路径
DATA_DIR = Path(__file__).parent.parent / "data"
REPORTS_DIR = Path(__file__).parent.parent / "reports"

def fetch_weibo_hotspots(limit=10):
    """抓取微博热搜"""
    # 使用 news-aggregator-skill
    import subprocess
    result = subprocess.run(
        ["python3", "/root/.openclaw/workspace/skills/news-aggregator-skill/scripts/fetch_news.py",
         "--source", "weibo", "--limit", str(limit), "--deep"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return json.loads(result.stdout)
    return []

def fetch_zhihu_hotspots(limit=10):
    """抓取知乎热榜"""
    import subprocess
    result = subprocess.run(
        ["python3", "/root/.openclaw/workspace/skills/news-aggregator-skill/scripts/fetch_news.py",
         "--source", "v2ex", "--limit", str(limit), "--deep"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return json.loads(result.stdout)
    return []

def fetch_toutiao_hotspots(limit=10):
    """抓取头条热文"""
    import subprocess
    result = subprocess.run(
        ["python3", "/root/.openclaw/workspace/skills/news-aggregator-skill/scripts/fetch_news.py",
         "--source", "tencent", "--limit", str(limit), "--deep"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return json.loads(result.stdout)
    return []

def analyze_hotspots(data):
    """分析热点数据"""
    analysis = {
        "timestamp": datetime.now().isoformat(),
        "total_count": len(data),
        "platforms": {},
        "top_hotspots": []
    }
    
    # 按平台分类
    for item in data:
        source = item.get("source", "unknown")
        if source not in analysis["platforms"]:
            analysis["platforms"][source] = []
        analysis["platforms"][source].append(item)
    
    # 按热度排序
    sorted_data = sorted(data, key=lambda x: int(x.get("heat", 0)), reverse=True)
    analysis["top_hotspots"] = sorted_data[:10]
    
    return analysis

def generate_report(analysis):
    """生成热点报告"""
    report = f"""# 热点追踪报告

**时间**: {analysis['timestamp']}

---

## 热点概览

- 总热点数: {analysis['total_count']}
- 平台数: {len(analysis['platforms'])}

---

## TOP 10 热点

| 排名 | 热点 | 热度 | 平台 |
|------|------|------|------|
"""
    
    for i, item in enumerate(analysis['top_hotspots'], 1):
        title = item.get('title', '未知')
        heat = item.get('heat', '0')
        source = item.get('source', '未知')
        report += f"| {i} | {title} | {heat} | {source} |\n"
    
    report += """
---

## 平台分布

"""
    
    for platform, items in analysis['platforms'].items():
        report += f"### {platform}\n\n"
        report += f"- 热点数: {len(items)}\n\n"
    
    report += """
---

*由 Hotspot Tracker 自动生成*
"""
    
    return report

def save_data(data, filename="hotspots.json"):
    """保存数据"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    filepath = DATA_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 数据已保存: {filepath}")

def save_report(report, filename="hotspot_report.md"):
    """保存报告"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = REPORTS_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ 报告已保存: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="热点追踪工具")
    parser.add_argument("--all", action="store_true", help="抓取所有平台")
    parser.add_argument("--weibo", action="store_true", help="抓取微博热搜")
    parser.add_argument("--zhihu", action="store_true", help="抓取知乎热榜")
    parser.add_argument("--toutiao", action="store_true", help="抓取头条热文")
    parser.add_argument("--limit", type=int, default=10, help="抓取数量")
    parser.add_argument("--report", action="store_true", help="生成报告")
    
    args = parser.parse_args()
    
    data = []
    
    if args.all:
        print("🔥 抓取所有平台热点...")
        data.extend(fetch_weibo_hotspots(args.limit))
        data.extend(fetch_zhihu_hotspots(args.limit))
        data.extend(fetch_toutiao_hotspots(args.limit))
    elif args.weibo:
        print("🔥 抓取微博热搜...")
        data.extend(fetch_weibo_hotspots(args.limit))
    elif args.zhihu:
        print("🔥 抓取知乎热榜...")
        data.extend(fetch_zhihu_hotspots(args.limit))
    elif args.toutiao:
        print("🔥 抓取头条热文...")
        data.extend(fetch_toutiao_hotspots(args.limit))
    else:
        print("请指定抓取平台: --all, --weibo, --zhihu, --toutiao")
        return
    
    if data:
        save_data(data)
        
        if args.report:
            print("📊 分析热点数据...")
            analysis = analyze_hotspots(data)
            report = generate_report(analysis)
            save_report(report)
            print(f"\n✅ 完成! 共抓取 {len(data)} 个热点")

if __name__ == "__main__":
    main()