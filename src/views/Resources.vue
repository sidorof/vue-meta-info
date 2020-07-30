<template>
<v-container fluid>
  <v-card>
    <v-card-title class="text-h3 ml-4 pl-6">Resources</v-card-title>
    <v-row no-gutters>
    <v-col cols="3">
      <ResourcesList/>
    </v-col>
    <v-col cols="9" v-if="getResource">
      <v-card-title>{{ getResource.name }}</v-card-title>
      <ResourceHeading :heading="heading"/>
      <ResourceMethods
        :methods="methods"
        :modelClass="getResource.modelClass"
        :resourceType="resourceType"
      />
    </v-col>
    </v-row>
  </v-card>
</v-container>
</template>

<script>
import { mapGetters } from 'vuex'

import ResourcesList from '@/components/ResourcesList'
import ResourceHeading from '@/components/ResourceHeading'
import ResourceMethods from '@/components/ResourceMethods'
// import ResourceTable from '@/components/ResourceTable'

export default {
  name: 'Classes',
  components: {
    ResourcesList,
    ResourceHeading,
    ResourceMethods
    // ResourceTable
  },
  data: () => ({
    resourceName: null
  }),
  computed: {
    ...mapGetters({
      getResource: 'meta/getResource'
    }),
    heading () {
      if (this.getResource !== undefined) {
        const resource = this.getResource
        return {
          modelClass: resource.modelClass,
          urlPrefix: resource.urlPrefix,
          url: resource.url
        }
      }
      return null
    },
    methods () {
      if (this.getResource !== undefined) {
        const resource = this.getResource
        return resource.methods
      }
      return null
    },
    resourceType () {
      if (this.getResource !== undefined) {
        const resource = this.getResource
        if (resource.methods.get !== undefined) {
          if (resource.methods.get.queryString === undefined) {
            return 'single'
          } else {
            return 'collection'
          }
        }
      }
      return null
    }
  }
}
</script>
