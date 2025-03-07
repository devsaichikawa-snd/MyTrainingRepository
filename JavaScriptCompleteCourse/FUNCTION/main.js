// 関数の正体はオブジェクトである

// 関数宣言文
// function add(a, b) {
//   return a + b;
// }
// let result = add(1, 2);

// 名前付き関数式
// let sayHi = function hi() {
//   return 'hi';
// };

// 無名関数
// let sayHello = function () {
//   return 'Hello';
// };

// 関数とメソッド
// const person = {
//   name: 'satoshi',
//   sayHey: function () {
//     return 'Hey!';
//   },
// };
// console.log(person.sayHey());

// アロー関数
// const sayGood = (name) => {
//   return `Good ${name}!`;
// };

// アロー関数はただ一つの式である場合に限り、{}とreturnを省略できる
// const sayGood = (name) => `Good ${name}!`;

// アロー関数はparameterがただ一つだけの場合は、引数の丸括弧を省略できる
// const sayGood = name => `Good ${name}!`;

// defaultパラメータ
// const sayGood = (name, message = 'You win!') => `Good ${name}! ${message}`;
// console.log(sayGood('Satoshi'));

// レストパラメータ
// pythonでいう、def sum(*args)
// const sum = (...nums) => {
//   console.log(nums);
//   let total = 0;
//   for (let num of nums) {
//     total += num;
//   }
//   return total;
// };
// console.log(sum(1, 2, 3, 4, 5));

// コールバック関数
// const print = (callback) => {
//   // 引数として受け取った関数を実行する
//   callback('Good Job!');
// };
// print((text) => {
//   console.log(text);
// });

// JavaScriptの標準ライブラリ(GlobalObject)
// console.log(globalThis);

// objectのキーに指定できる内容
// const person = {
//   name: 'Satoshi', // 変数OK
//   age: 30, // 変数OK
//   greeting: function () {}, // 関数OK
//   const: 'const', // 予約語もOK
//   currentcity: 'Saitama', // 文字列もOK
//   3: 3, // int型もOK
//   3.1: 3.1, // float型もOK
//   interests: ['music', 'travel'], // arrayもOK
// };
// ただし、厳密にはキーは文字列として管理されている

// getterとsetter
// const pastaCalculator = {
//   servingSize: 60,
//   member: 4,
//   get total() {
//     // これがgetter "get [property名](){}"の記述を覚えよ
//     return this.servingSize * this.member;
//   },
//   set total(value) {
//     // これがsetter
//     this.member = value / this.servingSize;
//   },
// };
// pastaCalculator.total = 600; // 代入する値がsetterの引数として当てられる
// console.log(pastaCalculator.total); // ←プロパティとして呼び出せる

// プロトタイプチェーン
// const obj = {
//   a: 1,
//   b: 2,
// };
// console.log(obj);

// プロトタイプの生成
// const obj2 = Object.create({ a: 1, b: 2 });
// console.log(obj2);

// コンストラクタ関数
// 記述はパスカルケース
// 記述するときはアロー関数を使用しない
// const User = function (name, age) {
//   // this = Object.create(User.prototype); を実行している
//   this.name = name;
//   this.age = age;
//   this.greeting = function () {
//     return `初めまして、${this.name}!! 私は${this.age}歳です`;
//   };
//   // return this; を実行している
// };
// 呼出し
// const user1 = new User('Satoshi', 28);

// クラス構文
class User {
  // 省略記法のメソッドのみ定義が可能。変数やobjectは定義できない。

  // (Public)フィールド letやconstは不要 尚、constructorよりも先に読み込まれる。原則として先頭に記述しよう
  id = 1;
  birthday = '1990/12/25';
  static department = 'development'; // 静的フィールド
  #prefecture = 'Saitama'; // privateフィールド class内からしかアクセスできない

  constructor(name, age) {
    // 特殊メソッド
    // コンストラクタメソッド内にのみ属性値を定義可能
    // newされたときに最初に実行される
    this.name = name;
    this.age = age;
    this.#prefecture;
  }
  get getName() {} // getter
  set setName(newName) {} // setter
  static add() {} // 静的メソッド。getterやsetterにも付けられる
  greeting() {}
  post() {}
  #rename() {} // privateメソッド
}
const user = new User(); // クラスはnewして使う
// staticのフィールドやメソッドはnewしなくても呼び出せる

// classの継承
// 親クラス(Superクラス)
class Animal {
  // publicフィールド
  age = 0;
  constructor(age) {
    this.age = age;
  }
  // メソッド
  eat() {
    console.log('eat now');
  }
}

// Animalクラスを親とし、子クラス(Subクラス)を定義する
class Bird extends Animal {
  // privateフィールドおよびprivateメソッドは子クラスでは利用できない
  name = 'pi';
  constructor() {
    // 子クラスでもコンストラクタ関数を定義する場合、親クラスのコンストラクタ関数を呼び出す必要がある
    super();
  }
  // OverRide
  eat() {
    super.eat();
    console.log('I eat bird!');
  }
  fly() {
    console.log('I can fly!');
  }
}
const bird = new Bird(3);
bird.eat();
