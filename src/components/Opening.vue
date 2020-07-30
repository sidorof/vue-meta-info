<template>
  <v-container>
    <v-card
      class="mx-auto"
      max-width="400"
    >
      <v-img
        src="landscapes-with-lake-and-clouds.jpg"
        alt="pic and Flask-RESTFul-DBBase title"
        class="white--text align-front"
        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
      >
        <v-card-title class="pl-10 text-h2">Flask</v-card-title>
        <v-card-title class="pl-15 text-h2 text-center">-RESTful</v-card-title>
        <v-card-title class="pl-15 text-h2">-DBBase</v-card-title>
      </v-img>
      <v-card-text class="text--primary">
        {{ intro }}
      </v-card-text>
      <v-card-actions>
        <v-btn
          v-for="(item, i) in items"
          :key="i"
          text large
          color="primary"
          :href="item.href"
        >
          {{ item.text }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Opening',
  components: {
  },

  data: () => ({
    intro: 'This app provides an example of meta information about backend resources created by Flask-RESTful-DBBase. For each resource (endpoint) and for each HTTP method, the inputs and responses can be detailed.',
    items: [
      { text: 'Resources', href: '/resources' },
      { text: 'DBBase Classes', href: '/classes' }
    ]
  }),
  computed: {}
}
</script>
