<template>
  <v-container>
    <v-card
      class="tile rounded-t-xl pl-3">
        <v-simple-table
          dense
          v-if="resourceList !== undefined"
          max-height="800px"
        >
          <template v-slot:default>
            <tbody>
              <tr
                v-for="(resource, i) in resourceList"
                :key="resource.name"
                @click="calcResource(i, resource.name)"
              >
                <td >{{ resourceName(resource.name) }}</td>
             </tr>
            </tbody>
            </template>
        </v-simple-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { fmtName } from '@/lib/common'

export default {
  name: 'ResourcesList',
  data: () => ({
    idx: null
  }),
  mounted: function () {
    this.loadResources()
  },
  computed: {
    ...mapGetters({
      getResources: 'meta/getResources',
      getResource: 'meta/getResource'
    }),
    resourceList () {
      var tmpList = []
      if (this.getResources !== undefined && this.getResources !== null) {
        for (const name in this.getResources) {
          tmpList.push({ name: name })
        }
      }

      const compare = (a, b) => {
        const nameA = a.name
        const nameB = b.name
        if (nameA > nameB) {
          return 1
        } else {
          return -1
        }
      }

      return tmpList.sort(compare)
    }
  },
  methods: {
    ...mapActions({
      clearResource: 'meta/clearResource',
      loadResources: 'meta/loadResources',
      loadResource: 'meta/loadResource'
    }),
    setResource (resource) {
      this.clearResource()
      this.loadClass({ name: resource })
    },
    calcResource (i, name) {
      // 'i' left here on purpose for now
      this.idx = i
      this.clearResource()
      const fullResource = this.getResources[name]
      this.loadResource(fullResource)
    },
    resourceName (name) {
      return fmtName(name)
    }
  }
}
</script>
