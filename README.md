# 雑魚寝日和 — 確認用サイト

4i RADIOのモキュメンタリーに登場する架空のUTAU音源配布サイトです。実在の音源配布サイトではありません。Since 2010、2010〜2014年の記事・更新日は作中設定で、現実の制作・公開日ではありません。本実装の制作日は2026-10-12です。日記の出来事と具体的日付は草案段階の演出案です。

## 確認
ZIPを展開して index.html をブラウザで開いてください。ビルド・外部フォント・外部ライブラリは不要です。8ページとも静的HTMLです。

## 公開状態
GitHub Pagesで公開中：https://zakone-biyori.github.io/
すべて相対パスで構成しています。

## 編集
日記は data/diary.json、更新履歴は data/history.json に分離しています。修正後は `python3 tools/rebuild_data.py` を実行すると対応HTMLを再生成します。その他の文章は各HTMLを直接編集できます。

## 画像差し替え
以下のパスへ画像を置くと、自動で枠を実画像に置き換えます。画像未提供時は中立な枠を表示します。画像の生成はしていません。

| ファイル | 掲載箇所 |
|---|---|
| assets/top-zakone.png | TOPとGALLERYのトップ絵 |
| assets/sema.png | セマ立ち絵 |
| assets/love.png | ラブ立ち絵 |
| assets/samu.png | サム立ち絵 |
| assets/gallery/initial-2010.png | 初期立ち絵 |
| assets/gallery/redesign-2011.png | 新公式立ち絵 |
| assets/gallery/doodle.png | らくがき |
| assets/gallery/fanart-01.png | いただきもの1 |
| assets/gallery/fanart-02.png | いただきもの2 |
| assets/banner-200x40.png | 自サイトのバナー |
| assets/banner-mutual-88x31.png | 相互リンクバナー |

## 確認・追記待ち
- 画像全11ファイル、提供画像の作者クレジット。
- 具体的な更新日・日記の日付は原稿の仮案をそのまま実装。
- 利用規約は原稿の導入文のみ。再配布・商用利用などの許諾は作成していません。
- 管理人連絡先、絵描きさんの名前、各キャラクターの年齢・数値・音源仕様は未掲載。
- LINKの外部リンク3つは安全な `.invalid` ドメイン。接続できないのは意図した演出です。
- 実ダウンロード、偽ZIP、外部送信、解析、保存機能はありません。

## 2026-10-18 素材反映
TOP、初期立ち絵、現在のラブ・サムを反映。セマの現行立ち絵は受け取り待ち。作中の更新履歴は変更していません。
