# my-junkyard

## 自動コードレビューワークフロー

このリポジトリには、GitHub Actionsを使用した自動コードレビューシステムが実装されています。

### 機能
- ブランチへのプッシュ時の自動コードレビュー
- 多言語対応 (Python, JavaScript, Go, Java, PHP, Ruby, Rust など)
- セキュリティスキャン
- プルリクエストへの自動コメント

詳細については [.github/CODE_REVIEW.md](.github/CODE_REVIEW.md) を参照してください。

### テストファイル
- `test_sample.py` - Python コードのテスト用
- `test_package.json` - JSON 形式の検証用