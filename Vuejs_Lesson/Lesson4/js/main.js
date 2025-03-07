const app = Vue.createApp({
  data: () => ({
    isLarge: true,
    hasError: false,
    largeClass: 'large',
    dangerClass: 'text-danger',
    classObject: {
      large: true,
      'text-danger': true,
    },
    largeClassPara3: {
      large: true,
      'bg-gray': true,
    },
    dangerClassPara3: {
      'text-danger': true,
    },
    isLargePara3: true,
    color: 'blue',
    fontSize: 36,
    styleObject: {
      color: 'green',
      fontSize: '48px',
    }
  }),
})

app.mount('#app')
