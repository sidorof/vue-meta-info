<template>
  <v-container fluid>
    <v-card-title class="text-h2 ml-4 pl-6">Classes</v-card-title>
    <v-divider></v-divider>
    <v-row no-gutters>
    <v-col
      cols="3"
    >
      <ClassList/>
    </v-col>
    <v-col cols="9" md="8" v-if="getClass">
      <ClassTable/>
    </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

import ClassList from '@/components/ClassList'
import ClassTable from '@/components/ClassTable'

export default {
  name: 'Classes',
  components: {
    ClassList,
    ClassTable
  },
  computed: {
    ...mapGetters({
      getClass: 'meta/getClass'
    })
  }
}
</script>
