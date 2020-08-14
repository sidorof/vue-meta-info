<template>
  <v-container>
    <v-card max-width="500px">
      <v-simple-table dense v-if="heading !== undefined">
        <template v-slot:default>
          <tbody>
           <tr
            v-for="resource in headingList"
            :key="resource.key"
           >
              <td >{{ resource.key }}</td>
              <td class="font-weight-bold">{{ resource.value }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'ResourceHeading',
  props: ['heading'],
  data: () => ({
  }),
  computed: {
    headingList () {
      return [
        { key: 'Model Class', value: this.heading.modelClass },
        { key: 'Url Prefix', value: this.heading.urlPrefix },
        { key: 'Base Url', value: this.heading.baseUrl }
      ]
    }
  }
}
</script>
