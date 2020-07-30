<template>
  <v-card >
    <v-card-title>URL</v-card-title>
    <v-card-text class="ml-4 pl-5 font-weight-bold">
      {{ getCurrentMethod.url}}
    </v-card-text>
    <v-card class="pb-4">
      <v-card-title>
        Requirements
        <div class="pl-1 text-body-1"> (Method Decorators)</div>
      </v-card-title>
      <div
        class="ml-4 pl-5 font-weight-bold"
        v-if="getCurrentMethod.requirements !== []"
      >
        {{ requirements }}
      </div>
    </v-card>
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

export default {
  name: 'Single',
  props: ['modelClass'],
  components: {
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
