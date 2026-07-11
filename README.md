# Network CIDR Tool

ネットワークエンジニア向けの簡単なPython CLIツールです。

## 概要

CIDR表記を入力すると、次の情報を表示します。

- ネットワークアドレス
- ブロードキャストアドレス
- サブネットマスク
- 利用可能ホスト数
- 利用可能範囲

## 使い方

```bash
python3 network_tool.py 192.168.1.0/24
```

## 出力例

```text
CIDR: 192.168.1.0/24
Network address: 192.168.1.0
Broadcast address: 192.168.1.255
Subnet mask: 255.255.255.0
Host count: 254
Usable range: 192.168.1.1 - 192.168.1.254
```

## 開発環境

- Python 3.9+
- 標準ライブラリのみ使用

## GitHubに公開する手順

```bash
git init
git add .
git commit -m "Initial commit"
```

その後、GitHubで新しいリポジトリを作成し、以下を実行します。

```bash
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```
