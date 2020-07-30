<template>
  <v-container>
    <v-card
      class="tile rounded-t-xl pl-3">
      <v-simple-table
        dense
        v-if="getClassList !== undefined"
        height="800px"
      >
        <template v-slot:default>
          <tbody>
            <tr
              v-for="cls in getClassList"
              :key="cls"
              @click="setClass(cls)"
            >
              <td >{{ cls }}</td>
            </tr>
          </tbody>
         </template>
      </v-simple-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ClassList',
  data: () => ({}),
  mounted: function () {
    this.loadClassList()
  },
  computed: {
    ...mapGetters({
      getClassList: 'meta/getClassList',
      getClass: 'meta/getClass'
    })
  },
  methods: {
    ...mapActions({
      clearClass: 'meta/clearClass',
      loadClassList: 'meta/loadClassList',
      loadClass: 'meta/loadClass'
    }),
    setClass (cls) {
      this.clearClass()
      this.loadClass({ name: cls })
      // if (this.getClass(cls) === undefined) {
      //   this.loadClass({ name: cls })
      // }
    }
  }
}
</script>
