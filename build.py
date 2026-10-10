#!/usr/bin/env python3
"""Build a Shadowrocket profile from Johnshall's upstream whitelist config."""
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
UPSTREAM = "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_whitelist_ad.conf"
PROFILE_URL = "https://raw.githubusercontent.com/lihuacai168/shadowrocket-la1-jp/main/sr_top500_whitelist_ad_la1_jp.conf"

GROUPS = """[Proxy Group]
# These filters select nodes from the separately imported subscriptions.
# Import nodes whose names start with LA1 and JP respectively.
美国节点 = select,policy-regex-filter=^LA1,select=0
加密货币-JP = select,policy-regex-filter=^JP,select=0

"""


def main() -> None:
    with urlopen(UPSTREAM, timeout=45) as response:
        source = response.read().decode("utf-8-sig")

    if "[General]\n" not in source or "[Rule]\n" not in source:
        raise SystemExit("Upstream Shadowrocket config is missing expected sections")
    if "update-url =" not in source:
        source = source.replace("[General]\n", f"[General]\nupdate-url = {PROFILE_URL}\n", 1)
    else:
        lines = source.splitlines()
        source = "\n".join(
            f"update-url = {PROFILE_URL}" if line.startswith("update-url =") else line
            for line in lines
        ) + "\n"

    source = source.replace("[Rule]\n", GROUPS + "[Rule]\n", 1)
    custom_rules = (ROOT / "custom-rules.conf").read_text(encoding="utf-8").strip()
    source = source.replace("[Rule]\n", f"[Rule]\n{custom_rules}\n", 1)

    required = [
        "[Proxy Group]",
        "美国节点 = select,policy-regex-filter=^LA1,select=0",
        "加密货币-JP = select,policy-regex-filter=^JP,select=0",
        "DOMAIN-SUFFIX,binance.com,加密货币-JP",
        "DOMAIN-SUFFIX,youtube.com,美国节点",
        "DOMAIN-SUFFIX,openai.com,美国节点",
        f"update-url = {PROFILE_URL}",
    ]
    missing = [item for item in required if item not in source]
    if missing:
        raise SystemExit(f"Generated profile is missing expected config: {missing}")

    (ROOT / "sr_top500_whitelist_ad_la1_jp.conf").write_text(source, encoding="utf-8")
    print(f"Wrote profile with {len(source.splitlines())} lines")


if __name__ == "__main__":
    main()
