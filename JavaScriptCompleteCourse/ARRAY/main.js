// 配列の話
// 配列を作成するときは、①indexは密にする ②リテラルの型をそろえることを意識すること

// 単純な配列
let fluits = ['apple', 'banana', 'grape'];

// 多次元配列
let num = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

// 空の配列を作成する
let job = new Array();
let job2 = [];

// スプレッド構文
let foods = [...fluits]; // 浅いコピー
foods.push('orange'); // 配列に要素を追加する

// 分割代入
const user = ['satoshi', 28];
let [userName, age] = user; // アンパッキングされる

// 配列を変更するメソッド
let testList = new Array();
testList.push('item1'); // 配列の末尾に要素を追加する
testList.push('item2');
testList.push('item3');
testList.pop(); // 配列の末尾の要素を削除し、削除した要素を返す(引数指定なしの時は末尾)
testList.unshift('item4'); // 配列の先頭に要素を追加する
testList.shift(); // 配列の先頭の要素を削除し、削除した要素を返す(引数指定なしの時は先頭)
// shiftとunshiftは内部処理が遅いため、あまり使わない。基本はpushとpop

// 配列のようなオブジェクト
let listObj = {
  0: 0,
  1: 1,
  2: 2,
  3: 3,
  length: 4,
};

// object → list にする
let newList = Array.from(listObj); // object側に"length"キーワードが無いと空の配列になってしまう。

/* Arrayのメソッド */
// splice 配列の任意の箇所に要素を追加・削除する(非破壊的)
// array.splice(始点, 対象個数, 置換え要素) -> 削除した要素を返す
let testItems = [1, 2, 3, 4, 5];
// testItems.splice(1, 2); // インデックス1から要素を2連続して削除する
testItems.splice(1, 1, 10); // インデックス1を削除し、インデックス1の箇所に10を挿入する

// fill
// copyWithin
// reverse 配列の並び順を逆順にする
// sort 昇順・降順で並び替えができる
// slice 要素の切り取り array.slice(始点, 終点)
// concat 配列の結合
// join 配列の結合
// indexOf 指定した要素のindexを取得する。同一要素が存在する場合は、最初にヒットするインデックスが返る
// includes 指定した要素が配列に含まれているかを調べる booleanで返す

// map
let testItems2 = [0, 1, 2, 3, 4];
let result = testItems2.map((item) => {
  return item * 10;
});

// flat 2~多次元配列を1次元配列にする

// filter
let testFilterList = [0, 1, 2, 3, 4, 5];
let resultFilter = testFilterList.filter((item) => {
  return item > 3; // 3より大きい要素を返す
});
// console.log(resultFilter);

// reduce

// findとfindIndex
// findメソッドは配列から該当の要素を見つけて返す。ただし要素に存在しない場合は、undefindが返る
let testFindList = ['a', 'b', 'c'];
let resultFind = testFindList.find((item) => {
  return item == 'c';
});
// console.log(resultFind);

// forEach 配列の繰り返し処理 メソッドからの返り値は無し。
let testForEachList = [0, 1, 2, 3, 4, 5, 6];
testForEachList.forEach((item) => {
  console.log(item);
});
