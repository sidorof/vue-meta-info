<template>
  <v-card>
  <v-simple-table dark dense v-if="getFields !== undefined">
    <template v-slot:default>
      <thead class="primary">
        <tr>
          <th class="white--text">Name</th>
          <th class="white--text text-sm-caption text-md-body-1">Type</th>
          <th v-if="columns.has('format')" class="white--text text-sm-caption text-md-body-1">Format</th>
          <th v-if="columns.has('readOnly')" class="white--text text-sm-caption text-md-body-1">ReadOnly</th>
          <th v-if="columns.has('primary_key')" class="white--text text-sm-caption text-md-body-1">Primary Key</th>
          <th v-if="columns.has('foreign_key')" class="white--text text-sm-caption text-md-body-1">Foreign Key</th>
          <th v-if="columns.has('nullable')" class="white--text text-sm-caption text-md-body-1">Nullable</th>
          <th v-if="columns.has('default')" class="white--text text-sm-caption text-md-body-1">Default</th>
          <th v-if="columns.has('onupdate')" class="white--text text-sm-caption text-md-body-1">On Update</th>
          <th v-if="columns.has('info')" class="white--text text-sm-caption text-md-body-1">Info</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="field in getFields" :key="field.name">
          <td class="font-weight-bold text-sm-caption text-md-body-1">{{ field.name }}</td>
          <td>{{ field.type }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('format')">{{ field.format }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('readOnly')">{{ field.readOnly }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('primary_key')">{{ field.primary_key }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('foreign_key')">{{ field.foreign_key }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('nullable')">{{ field.nullable }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('default')">{{ field.default }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('onupdate')">{{ field.onupdate }}</td>
          <td class="text-sm-caption text-md-body-1" v-if="columns.has('info')">{{ field.info }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  </v-card>
</template>

<script>
export default {
  props: ['fields'],
  name: 'FieldsTable',
  data: () => ({
    columns: new Set()
  }),
  computed: {
    getFields () {
      var fields = []
      for (const name in this.fields) {
        var fmtField = { name: name, ...this.fields[name] }

        for (const key in fmtField) {
          this.columns.add(key)
        }
        if (fmtField.relationship === undefined) {
          fields.push(fmtField)
        }
      }
      return fields
    }
  }
}
</script>
