# Shadowrocket LA1 + JP split routing

A Shadowrocket (`.conf`) profile based on Johnshall's `sr_top500_whitelist_ad.conf`, with two node-name-filtered proxy groups and custom site-routing rules:

- YouTube / Google video and OpenAI / Anthropic / Gemini domains → `美国节点` (LA1)
- Common crypto exchanges → `加密货币-JP` (JP)
- Other traffic keeps the upstream whitelist config's original behavior.

## Install

1. Import two **proxy subscriptions** into Shadowrocket. The LA1 feed's node names start with `LA1`; the JP feed's names start with `JP`. Keep those prefixes so the groups can find the right nodes.
2. Add the config profile URL below in Shadowrocket's Config page (the `+` button → Download from URL). Select/use this config after it downloads.
3. In Rule mode, select a LA1 node in `美国节点` and a JP node in `加密货币-JP`. Domain rules then direct the matching apps/sites to the appropriate group.

The config repository intentionally contains **no server credentials**. Proxy subscriptions are separate, private links and must not be committed here.

## Update upstream rules

Run `python3 build.py` to download the latest upstream whitelist/ad profile and apply `custom-rules.conf` plus the proxy groups. Commit the rebuilt `sr_top500_whitelist_ad_la1_jp.conf` to publish an update.

## Attribution and license

The generated profile is derived from [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever), whose upstream profile is licensed under CC BY-SA 4.0. This derivative is also distributed under CC BY-SA 4.0; see `LICENSE`.
