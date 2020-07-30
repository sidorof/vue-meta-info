<template>
  <v-container>
    <v-card class="px-3 my=0">
      <v-card-title>
        {{ modelClass }} Relationship
      </v-card-title>
      <v-card class="d-flex flex-row pa-3 tile flat">
        <div class="body-1">Relation Type:</div>
        <div class="mx-3 font-weight-bold"> {{ relation.relationship.type }}</div>
        <div class="body-1">Entity:</div>
        <div class="mx-3 font-weight-bold"> {{ relation.relationship.entity }}</div>
      </v-card>
      <v-card class="mt-3" color="#ddd">
        <div class="pl-3 pt-2 font-weight-bold">
          {{ relation.relationship.entity }} Fields
        </div>
        <FieldsTable :fields="relation.relationship.fields"/>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
import FieldsTable from './FieldsTable'

export default {

  props: ['relation', 'modelClass'],
  name: 'relationship',
  components: {
    FieldsTable
  },
  data: () => ({
  }),
  computed: {
    getFields () {
      var tmpFields = []
      for (var name in tmpFields) {
        tmpFields.push({ name: name, ...tmpFields[name] })
      }
      return tmpFields
    }
  }
}
</script>
