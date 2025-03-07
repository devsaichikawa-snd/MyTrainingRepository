
const app = Vue.createApp({
  data: () => ({
    message: 'Hello Vue.js!',
    km: 0,
    m: 0,
    firstName: '',
    lastName: '',
    fullName: '',
    firstNameComputed: '',
    lastNameComputed: '',
    colors: [
      {name: 'Red'},
      {name: 'Green'},
      {name: 'Blue'},
      ],
  }),
  computed: {
    fullNameComputed: function(){
      return this.firstNameComputed + ' ' + this.lastNameComputed
    },
  },
  watch: {
    message: function(newValue, oldValue){
      console.log('new: %s, old: %s', newValue, oldValue)
    },
    km: function(value){
      console.log('value')
      this.km = value
      this.m = value * 1000
    },
    m: function(value){
      console.log('value')
      this.km = value / 1000
      this.m = value
    },
    firstName: function(value){
      this.fullName = value + ' ' + this.lastName
    },
    lastName: function(value){
      this.fullName = this.firstName + ' ' + value
    },
    colors: {
      handler: function(newValue, oldValue){
        console.log('Update!')
      },
      deep: true,
    },
  },
  methods: {
    onClick: function(){
      this.colors[1].name = 'White'
    }
  }
})

app.mount('#app')
