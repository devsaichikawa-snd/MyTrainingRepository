

// buttonの情報を取得する
const btn = document.querySelector('#btn');

// buttonに埋め込むイベント
function changeColor() {
    this.style.color = 'red';
}
function changeBGColor() {
    this.style.backgroundColor = 'green';
}

// ボタンにイベントをセット
// btn.addEventListener('click', changeColor)
// btn.addEventListener('click', changeBGColor)

btn.onclick = changeColor;

// ボタンのイベントを削除
// btn.removeEventListener('click', hello)
