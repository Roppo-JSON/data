# 法律データ

[![LANGUAGE](https://img.shields.io/badge/Python-3.8.0-blue.svg)](https://docs.python.org/3/)
[![LICENSE](https://img.shields.io/badge/License-Apache%202-orange.svg)](http://www.apache.org/licenses/LICENSE-2.0)

[![GitHub Actions](https://github.com/Roppo-JSON/data/workflows/Formatter%20Test/badge.svg)](https://github.com/Roppo-JSON/data/actions)

Roppo-JSON で使用する法律データはすべて [e-Gov](https://www.e-gov.go.jp/) のものを使用しています。

## フォーマット

[schema.json](./schema.json) を参照にしてください。 [validator.py](./validator.py) をパスし、かつ e-Gov から取得したデータを基にしていればどのようなパースコードになっても構いません。ただし、可読性やメンテナンス性に配慮してください。ふたつ以上の法令のパースに利用する関数は `utils` モジュールに移植すると良いかもしれません。

## LICENSE

See [LICENSE](./LICENSE) (Exclude under [/original](./original/))

(c) 2019 Roppo-JSON.
