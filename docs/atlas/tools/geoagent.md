---
title: GeoAgentとOpenGeoAgent
category: tools
updated: 2026-11-01
---

# GeoAgentとOpenGeoAgent

opengeosのGeoAgentは、地理空間Pythonライブラリや地図ウィジェット、QGISの道具をLLMから使うための共通エージェント層である。OpenGeoAgentは関連するQGISプラグインで、Mapsukeとは別のプロジェクトである。

利用するPython環境へ必要な依存関係を導入し、AI提供元やモデルを設定する。QGISで使う場合は、QGISが使うPython環境に合わせる。AIへの指示だけで地理データや分析結果の正しさが保証されるものではない。

## 依存パッケージの名前を確認する

2026年10月31日UTC公開のv1.9.1は、GeoAgent[geoai]またはGeoAgent[all]が本来のgeoai-pyではなく、無関係なプレースホルダーgeoaiを導入していた不具合を修正した。公式が示す対象は1.0.0〜1.9.0である。

公式は対象利用者に更新を案内し、誤ったパッケージが導入済みの場合はpip uninstall geoaiによる削除を指示している。削除対象があるか、どのPython環境かを確認して適用する。不具合の説明であり、悪意あるパッケージと発表されたものではない。Requestyプロバイダーの追加も含む。

本Atlasではインストールや削除、AI操作の試験をしていない。機能追加の規模よりも、利用する依存関係の正確さに影響する更新として記録する。

## 次に読む

- [GIS操作の依頼設計](../concepts/location-ai.md)：対象・条件・結果確認を決める。
- [Mapsuke](mapsuke.md)：別方式のQGIS操作支援。

## 出典

- [GeoAgent README](https://github.com/opengeos/GeoAgent)（2026-11-01確認）
- [v1.9.1](https://github.com/opengeos/GeoAgent/releases/tag/v1.9.1)（2026-11-01 GitHub公式APIで本文・公開日時確認）
