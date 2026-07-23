from datetime import datetime
import requests

all_rules = []
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 订阅头部（AdGuard、uBlock 软件内显示名称：融合规则手机版-Jason）
header = f"""
! Title: 融合规则手机版-Jason
! Homepage: https://github.com/rose5200/my-ad-filter
! Description: HalfLife移动端规则+EasyList基础广告+EasyPrivacy隐私防护+Cookie弹窗拦截+自定义恶意跳转黑名单
! Last modified: {now}
"""
all_rules.append(header)

# 上游4套完整规则源，已修复HalfLife 404报错
source_list = [
    ("HalfLife 移动端", "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt"),
    ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
    ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
    ("I don't care cookies", "https://www.i-dont-care-about-cookies.eu/abp/")
]

# 自动逐个拉取上游规则，异常自动打印失败日志
for name, url in source_list:
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        all_rules.append(f"\n! ========== {name} ==========\n")
        all_rules.append(resp.text)
    except Exception as err:
        all_rules.append(f"\n! 【拉取失败】{name} | {url} | 错误：{str(err)}\n")

# 你的专属自定义跳转拦截规则
personal_rules = """
! ========== 个人自定义拦截黑名单 ==========
||viiraipj.com/h/$document,redirect
||ayhal.com/sm-click$document,redirect
"""
all_rules.append(personal_rules)

# 生成最终聚合规则文件
with open("mobile_final.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_rules))
