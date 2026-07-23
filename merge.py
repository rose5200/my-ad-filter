import requests

# 固定4条你需要的规则
rule_urls = [
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt",
    "https://easylist-downloads.adblockplus.org/easylist.txt",
    "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    "https://www.i-dont-care-about-cookies.eu/abp/"
]

unique_rules = set()

for url in rule_urls:
    try:
        res = requests.get(url, timeout=12)
        content = res.text
        for row in content.splitlines():
            row = row.strip()
            # 过滤注释、空行
            if not row or row.startswith("!"):
                continue
            # 剔除专属语法保证AdGuard兼容
            if row.startswith(("#%#", "##+js")):
                continue
            unique_rules.add(row)
    except Exception as e:
        print(f"拉取失败 {url}")

final = sorted(list(unique_rules))

# 输出最终规则文件
with open("mobile_final.txt", "w", encoding="utf-8") as f:
    f.write("! 手机专用合并规则 HalfLife移动端+EasyList+EasyPrivacy+Cookie\n")
    f.write("! 自动定时更新，已全局去重\n\n")
    f.write("\n".join(final))
