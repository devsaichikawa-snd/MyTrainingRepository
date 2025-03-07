let count = 0; // 変数宣言と初期化
count = 30;
const daysInWeek = 7; // 定数宣言と初期化

// 命名法則
let tomatoCount; // キャメルケース
let tomatocount; // 上とは別の変数になる小文字と大文字は識別される
let $tomato$Count; // $を使う
let _tomato_Count; // アンダースコアを使う
let tomatoCount7; // 数字を使う
// 良い書き方
let bananaCount; // 変数名定数名はキャメルケースがベストプラクティス

// 演算子
let additionResult = 2 + 5;
let result = 0;

// result = result + 10;
result += 10; // 上式の省略形

result++; // +1する前の値を返す
++result; // +1した後の値を返す

// 型
let number = 10;
number = -1;
number = 3.5;

let string1 = 'Hello';
const userName = 'Satoshi';
let string2 = string1 + userName;
string2 = `Good ${userName}!`; // ${変数名}で変数を文字列に入れられる。ただし、グレイブアクセントを使うこと

let string3 = "I'm Satoshi!";
string3 = "I'm Satoshi!";

// 型変換
let numStr = '10';
let numInt = Number(numStr);
let numInt2 = parseInt(numStr);

let numNum = 111;
let numStr1 = String(numNum);
let numStr2 = numNum.toString();

// 配列
let array = ['apple', 'banana'];

// オブジェクト型
let coffee = {
  name: 'Chocolate', // 属性をプロパティと呼ぶ
  size: 350,
};
coffee.size = 400;

// nullとundifined
let non = null; // 存在しない(明示しないと設定されない)→明示的に何もないことを示したいときはNullを使用する
let userInfo = undefined; // 存在しない(暗黙的に設定される)

// 関数
// function add() {
//   console.log(1 + 1);
// }
// add();

// 関数と引数
function add(num1, num2) {
  return num1 + num2;
}
let returnValue = add(2, 3);
