# Hotspot Tracker - 热点追踪工具

自动抓取微博热搜、知乎热榜、头条热文，生成热点分析报告。

## 功能

- ✅ 自动抓取多平台热点数据
- ✅ 热度排名分析
- ✅ 热点趋势预测
- ✅ 生成JSON/Markdown报告
- ✅ 定时自动执行

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 抓取所有平台热点
python src/tracker.py --all

# 抓取微博热搜
python src/tracker.py --weibo

# 抓取知乎热榜
python src/tracker.py --zhihu

# 生成报告
python src/tracker.py --all --report
```

## 输出

- `data/hotspots.json` - 热点数据
- `reports/hotspot_report.md` - 热点报告

## 定时执行

```bash
# 每天早上8点自动执行
cron add "0 8 * * *" "python src/tracker.py --all --report"
```

## 版本

- v1.0.0 - 基础版本，支持微博、知乎、头条
- v1.1.0 - 增加趋势分析（付费版）

## 价格

- 免费版：基础热点抓取
- 付费版：99元/月，增加趋势分析、预测功能

## 作者

AI运营团队 - 一人公司自动化工具