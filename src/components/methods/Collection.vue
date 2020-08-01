<template>
  <v-card>
    <MethodHeading/>
    <v-card-title>Query Variables</v-card-title>
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
import MethodHeading from './MethodHeading'

export default {
  name: 'Single',
  props: ['modelClass'],
  components: {
    MethodHeading,
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
