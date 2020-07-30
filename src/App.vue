<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <router-link
          to="/"
          style="cursor: pointer">
          <div class="white--text">
            Meta Information
          </div>
        </router-link>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="/resources"
        text
      >
        <span class="mr-2">Resources</span>
        <v-icon>mdi-format-list-bulleted-square</v-icon>
      </v-btn>
      <v-btn
        href="/classes"
        text
      >
        <span class="mr-2">Classes</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {
    // HelloWorld
    // Classes
  },

  data: () => ({
  })
}
</script>
