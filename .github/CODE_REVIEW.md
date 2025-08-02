# GitHub Actions 自動コードレビューワークフロー

このリポジトリには、ブランチにコミットがプッシュされたときに自動でコードをレビューするGitHub Actionsワークフローが含まれています。

## 機能

### 🔍 自動トリガー
- **プッシュイベント**: main/master以外のブランチへのプッシュで実行
- **プルリクエスト**: main/masterブランチへのPRで実行

### 🛠️ コードレビュー機能

1. **Super-Linter による多言語対応**
   - Markdown, YAML, JSON, XML
   - Python, JavaScript, TypeScript, Go, Java, PHP, Ruby, Rust
   - HTML, CSS, Dockerfile, Bash scripts, SQL

2. **セキュリティスキャン**
   - Trivy による脆弱性スキャン
   - 結果はGitHubのSecurityタブに自動アップロード

3. **プルリクエストコメント**
   - レビュー結果の自動コメント
   - 変更されたファイルの統計
   - 推奨事項の提示

## ワークフローファイル

- **メインワークフロー**: `.github/workflows/code-review.yml`
- **設定ファイル**: `.github/linters/.super-linter.env`

## 使用方法

1. 任意のブランチにコードをプッシュ
2. GitHub Actionsが自動的に実行
3. Actionsタブでレビュー結果を確認
4. PRの場合は自動コメントでサマリーを確認

## カスタマイズ

`.github/linters/.super-linter.env` ファイルを編集することで、リンターの設定をカスタマイズできます。

## 対応言語・技術

- **プログラミング言語**: Python, JavaScript, TypeScript, Go, Java, PHP, Ruby, Rust
- **マークアップ・設定**: Markdown, YAML, JSON, XML, HTML, CSS
- **インフラ**: Dockerfile, Bash scripts, SQL
- **セキュリティ**: 脆弱性スキャン、機密情報検出

このワークフローにより、コードの品質とセキュリティが自動的に維持されます。