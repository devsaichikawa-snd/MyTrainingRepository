const app = Vue.createApp({
  data: () => ({
    counter1: 0,
    counter2: 0,
    counter3: 0,
    message: '',
    message2: '',
  }),
  methods: {
    clickHandler: function(event) {
      this.counter2++
    },
    clickHandler2: function(event) {
      this.counter3++
      console.log(event)
      console.log(event.target)
      console.log(event.target.tagName)
      console.log(event.target.innerHTML)
      console.log(event.target.type)
      console.log(event.target.id)
    },
    clickHandler3: function($event, message) {
      console.log(message)
      console.log($event)
      this.message = message
    },
    clickHandler4: function($event, message) {
      this.message2 = new Date().toLocaleTimeString()
    },
  },
})

app.mount('#app')
