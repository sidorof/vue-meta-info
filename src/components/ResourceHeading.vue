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
        { key: 'modelClass', value: this.heading.modelClass },
        { key: 'urlPrefix', value: this.heading.urlPrefix },
        { key: 'base url', value: this.heading.url }
      ]
    }
  }
}
</script>
