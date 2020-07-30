<template>
  <v-card>
    <v-card-title>{{ getCurrentMethod.url}}</v-card-title>
    <v-card flat>
      <v-card-title>
        Requirements
        <div class="pl-1 text-body-1"> (Method Decorators)</div>
      </v-card-title>
      <div class="ml-4 pl-4 font-weight-bold">
        {{ requirements }}
      </div>
    </v-card>
    <v-card-title>Queries</v-card-title>
    {{ getCurrentMethod.queryString }}
    <FieldsTable :fields="queryFields"/>

    <div v-if="responseRelations">
      <v-card-title>Response</v-card-title>
      <FieldsTable :fields="responseFields"/>
       <div
       v-for="(relation,i) in responseRelations"
       :key="i"
       >
         <Relationship
          :relation="relation"
          :modelClass="modelClass"
         />
       </div>
    </div>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import { fmtFieldsList, showRequirements } from '@/lib/common'
import FieldsTable from '@/components/FieldsTable'
import Relationship from '@/components/Relationship'

export default {
  name: 'Single',
  props: ['modelClass'],
  components: {
    FieldsTable,
    Relationship
  },
  data: () => ({
    queryFields: null,
    responseFields: null,
    responseRelations: null
  }),
  mounted () {
    this.setValues()
  },
  watch: {
    getCurrentMethod (val) {
      this.setValues()
    }
  },
  computed: {
    ...mapGetters({
      getCurrentMethod: 'meta/getCurrentMethod'
    }),
    requirements () {
      return showRequirements(
        this.getCurrentMethod.requirements)
    }
  },
  methods: {
    resetVars () {
      this.queryFields = null
      this.inputRelations = null
      this.responseFields = null
      this.responseRelations = null
    },
    setValues () {
      this.resetVars()
      this.queryFields = this.getCurrentMethod.queryString
      if (this.getCurrentMethod.responses.fields !== undefined) {
        const responseValues = fmtFieldsList(
          this.getCurrentMethod.responses.fields)
        this.responseFields = responseValues.fields
        this.responseRelations = responseValues.relations
      }
    }
  }
}
</script>
