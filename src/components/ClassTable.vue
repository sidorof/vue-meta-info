<template>
  <v-container>
    <v-card class="tile rounded-t-xl ">
      <v-card-title>{{ modelClass }}</v-card-title>
      <v-card height="50px" class="text-h4 text-center" v-if="error" color="error">{{ error }}</v-card>

      <div v-if="!loading && !error">
        <FieldsTable :fields="fields"/>
        <div v-for="(relation,i) in relations" :key="i">
          <Relationship :relation="relation" :modelClass="modelClass"/>
        </div>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { fmtFieldsList } from '@/lib/common'
import FieldsTable from '@/components/FieldsTable'
import Relationship from './Relationship'

export default {
  name: 'ClassTable',
  components: {
    FieldsTable,
    Relationship
  },
  data: () => ({
    modelClass: '',
    fields: {},
    relations: {}
  }),
  mounted () {
    const values = fmtFieldsList(this.getClass.properties)
    this.fields = values.fields
    this.relations = values.relations
    this.modelClass = this.getClass.name
  },
  computed: {
    ...mapGetters({
      loading: 'loading',
      error: 'error',
      getClass: 'meta/getClass'
    })
  }
}
</script>
