<template>
  <v-card >
    <MethodHeading/>
    <v-card-title>Inputs</v-card-title>
    <FieldsTable :fields="inputFields"/>
    <div
      v-for="(relation,i) in inputRelations" :key="i"
    >
      <Relationship
        :relation="relation"
        :modelClass="modelClass"
      />
    </div>

    <div v-if="responseFields">
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
    inputFields: null,
    inputRelations: null,
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
      this.inputFields = null
      this.inputRelations = null
      this.responseFields = null
      this.responseRelations = null
    },
    setValues () {
      this.resetVars()
      const inputValues = fmtFieldsList(this.getCurrentMethod.input)
      this.inputFields = inputValues.fields
      this.inputRelations = inputValues.relations

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
