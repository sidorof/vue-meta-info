<template>
  <v-container fluid>
    <v-card-title class="text-h3 ml-4 pl-6">Classes</v-card-title>
    <v-row no-gutters>
    <v-col
      cols="3"
    >
      <ClassList/>
    </v-col>
    <v-col cols="9" v-if="getClass">
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
