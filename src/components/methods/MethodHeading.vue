<template>
  <v-card flat>
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
        class="ml-4 pl-5 "
        v-if="getCurrentMethod.requirements !== []"
      >
        {{ requirements }}
      </div>
    </v-card>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import { showRequirements } from '@/lib/common'

export default {
  name: 'MethodHeading',
  props: ['modelClass'],
  computed: {
    ...mapGetters({
      getCurrentMethod: 'meta/getCurrentMethod'
    }),
    requirements () {
      return showRequirements(
        this.getCurrentMethod.requirements)
    }
  }
}
</script>
