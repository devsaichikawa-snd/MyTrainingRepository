// function hello(callback) {
//     console.log('hello' + callback());
// }

// function getName() {
//     return 'Ichikawa Satoshi';
// }

// hello(() => 'satoshi');


// hello(getName);


function dosomething(a, b, callback) {
    const result = callback(a, b);
    console.log(result);
}

function multiply(a, b) {
    return a * b;
}

dosomething(2, 3, multiply);






