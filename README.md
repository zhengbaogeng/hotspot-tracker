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

## 💰 赞助支持

如果这个工具对你有帮助，欢迎赞助支持！

### 赞助方式

- **GitHub Sponsors**: 点击仓库右侧的"Sponsor"按钮
- **微信支付**: 联系作者获取支付方式
- **支付宝**: 联系作者获取支付方式

### 赞助金额

- ⭐ **$5/月** - 基础赞助，感谢支持
- ⭐⭐ **$10/月** - 中级赞助，获得优先支持
- ⭐⭐⭐ **$15/月** - 高级赞助，获得付费版功能

### 赞助福利

- ✅ 优先获得新功能更新
- ✅ 专属技术支持
- ✅ 付费版功能解锁
- ✅ 定制化需求优先处理

---

**感谢您的支持！让AI工具帮助更多人！**

## 作者

AI运营团队 - 一人公司自动化工具

## 联系方式

- 邮箱：376130454@qq.com
- GitHub：https://github.com/zhengbaogeng