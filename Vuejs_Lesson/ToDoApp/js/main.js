
const app = Vue.createApp({ // オブジェクト化
  data: () => ({ // HTML側で用いる値を記述
    newItem: '',
    todos: [],
  }),
  methods: { // HTML側で用いる関数を記述
    addItem: function(){
      // console.log('Clicked')
      if(this.newItem === '') return
      let todo = {
        item: this.newItem,
        isDone: false,
      }
      this.todos.push(todo)
      this.newItem = ''
    },
    deleteItem: function(index){
      // console.log('delete!')
      // console.log(index)
      this.todos.splice(index, 1)
    },
  },
})

app.mount('#app') // id,classにマウント
