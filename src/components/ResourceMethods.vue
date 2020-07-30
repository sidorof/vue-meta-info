<template>
  <v-container>
    <v-card>
      <v-tabs
        v-model="tab"
        background-color="primary"
        dark
      >
        <v-tab
          v-for="item in items"
          :key="item.tab"
        >
          {{ item.tab }}
        </v-tab>
      </v-tabs>

       <v-tabs-items v-model="tab">
       <v-tab-item
        v-for="item in items"
        :key="item.tab"
      >
      <v-card flat>
        <Single
          :modelClass="modelClass"
          v-if="resourceType === 'single'"
        />
        <Collection
            :modelClass="modelClass"
            v-if="resourceType ===  'collection'"
        />
      </v-card>
       </v-tab-item>
       </v-tabs-items>
       <div v-if="resourceType">
        </div>
    </v-card>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'
import Single from './methods/Single'
import Collection from './methods/Collection'

export default {
  name: 'ResourceMethods',
  props: ['resourceType', 'methods', 'modelClass'],
  components: {
    Single,
    Collection
  },
  data: () => ({
    // tab: null,
  }),
  computed: {
    items () {
      var items = []
      for (const key in this.methods) {
        items.push({ tab: key })
      }
      return items
    },
    tab: {
      get () {
        return this.$store.state.meta.tab
      },
      set (value) {
        this.$store.commit('meta/setTab', value)
      }
    }
  },
  methods: {
    ...mapActions({
      clearCurrentMethod: 'meta/clearCurrentMethod',
      setCurrentMethod: 'meta/setCurrentMethod'
    })
  }
}
</script>
