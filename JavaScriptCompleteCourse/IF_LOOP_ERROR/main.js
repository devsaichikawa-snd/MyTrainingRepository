// if構文
let ok = false;
let maybeOk = true;
// if (ok) {
//   // ok がTrueの場合の処理
//   console.log('OK');
// } else if (maybeOk) {
//   // ok がfalseかつmaybeokがtrueの場合の処理
//   console.log('Maybe Ok...');
// } else {
//   // それ以外の処理
//   console.log('No');
// }

// "===" と "=="の違い
// 論理演算子 || 論理和、 && 論理積
// Null合体代入演算子

// 3項条件演算子
let flag = true;
let value = flag ? 'OK' : 'NG';

// Switch文
function vegetableColor(vegetable) {
  switch (vegetable) {
    case 'tomato':
      console.log('red');
      break;
    case 'banana':
      console.log('yellow');
      break;
    case 'onion':
      console.log('white');
      break;
    default:
      console.log('Not Found');
  }
  // if文では非常に冗長...
  // if (vegetable === 'tomato') {
  //   console.log('red');
  // } else if (vegetable === 'banana') {
  //   console.log('yellow');
  // } else if (vegetable === 'onion') {
  //   console.log('white');
  // }
}
// vegetableColor('apple');

// while文
// let count = 0;
// while (count < 10) {
//   console.log(count);
//   count += 1;
// }

// do-while文
// let count = 100;
// do {
//   console.log('Start');
//   count += 1;
// } while (count < 10);

// for文
// for (let i = 0; 10 > i; i++) {
//   console.log(i);
// }

// for-of文(配列の場合に使用することが多い)
const fruits = ['apple', 'banana', 'orange', 'mango', 'grape'];
// for (const fruit of fruits) {
//   console.log(fruit);
// }

// for-in文(オブジェクトに多い)
const coffee = {
  name: 'Caffee',
  size: 400,
  isHot: true,
};
// for (const key in coffee) {
//   console.log(key);
//   console.log(coffee[key]);
// }

// try-catch(try-catch-finally)
// pythonでいうところの「try-except-else-finally」
try {
  // 例外処理をcatchしたい処理
} catch {
  // 例外発生時の処理
} finally {
  // 必ず実行する処理
}

// throw エラーを作る
throw 'error';
