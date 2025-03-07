/* JavaScriptによるWebブラウザ操作 */

// alert('Hello'); // ポップアップを表示する
// confirm('Are you OK?'); // ポップアップを出す。 OK/キャンセル
// prompt('name', 'Satoshi'); // ポップアップを出す。入力可能

// location URLに移動する。URLのPerth
// history ページ履歴の戻る・先に進む

// URLのperth
// let url = new URL('https://www.youtube.com/');

// setTimeout 第2引数分待ってから、第1引数のcallback関数を実行する
// let timerId = setTimeout(() => {
//   console.log('Hello');
// }, 5000); // -> timerId = 1
// clearTimeout(timerId); // setTimeoutのキャンセル
// let timerId2 = setInterval(() => {
//   console.log('Hello');
// }, 1000);
// clearTimeout(timerId2);

// Intersection Observer API 無限スクロール、スクロール時の動的画面生成

// DOMのノードを取得する
let htmlElem = document.documentElement; // HTML要素を取得する
let headElem = document.head; // head要素を取得する
let bodyElem = document.body; // body要素を取得する

// 親子間のノードを取得する
let childNodes = document.childNodes; // 子ノードを全て取得する
let childNodesflag = document.childNodes[0].hasChildNodes(); // 子ノードの要素があるか確認する ->boolean

// 親子間の要素だけを取得する
// let elem = document.body.parentElement;

// 汎用的な要素取得方法 querySelector (新式)
// document.querySelector('css-selector') 「document(HTML)の中から指定したタグやCSS-Selectorを取ってくる」
let elem = document.querySelector('#hello'); // id 単数
let elem1 = document.querySelector('p'); // tag 単数
// 複数取得
let elems = document.querySelectorAll('p'); // tag 複数
let elems2 = document.querySelectorAll('.apple'); // class 複数

// querySelectorが出る前の書き方(旧式)
let elemOldWay = document.getElementById('hello'); // id属性
let elemOldWay2 = document.getElementsByName('good'); // name属性
let elemOldWay3 = document.getElementsByTagName('p'); // tag <></>
let elemOldWay4 = document.getElementsByClassName('apple'); // class属性

// DOMを操作する

// (注意)innerHTMLはXSSに気を付ける必要がある
// 要素を追加する※divタグを削除→新規追加の手順
document.querySelector('div').innerHTML = '<h2>Hi Added</h2>';
// 要素を追加 単純な追加
document
  .querySelector('div')
  .insertAdjacentHTML('beforeend', '<p>I am 28 years old.</p>');

// HTML要素を作成する(ノードを作成する)→DOMツリーに挿入する XSS対策もされている！
let p = document.createElement('p');
document.querySelector('div').append('Text is simple.'); // DOMツリーに挿入する
// document.querySelector('div').prepend(p);
// document.querySelector('div').before(p);
// document.querySelector('div').after(p);
