
const app = Vue.createApp({
  data: () => ({
    message: 'Hello Vue.js!',
    message_red: 'Hello <span style="color:red;">Vue.js!</span>',
    number: 100,
    ok: false,
    url: 'https://www.google.co.jp/',
    basePrice: 100,
  }),
  computed: {
    reversedMessage: function(){
      // 文字列の反転
      return this.message.split('').reverse().join('')
    },
    taxIncludedPrice: {
      get: function(){
        return this.basePrice * 1.1
      },
      set: function(value){
        this.basePrice = value / 1.1
      },
    },
    computedNumber: function(){
      return Math.random()
    },
  },
  methods: {
    clickHandler: function(event){
      // 文字列の反転
      this.message = this.message.split('').reverse().join('')
    },
    reversedMessageMethod: function(){
      // 文字列の反転
      return this.message.split('').reverse().join('')
    },
    methodNumber: function(){
      return Math.random()
    },
  },
})

app.mount('#app')
