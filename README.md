# EasyEncoding
## Usage
1. moduleをimport
2. 変換したいインスタンスを入力
3. 変換されたインスタンスがリターンされる

## Caution
* 変換可能なクラスはList, Dict, Str, Unicodeのみとなります
* 変換不能なクラスのインスタンスが入力された場合, TypeErrorが発生しますので, try等でエラーハンドリングを行うと良いでしょう