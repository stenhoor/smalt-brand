<script setup lang="ts">
// The stage badge at the top of a product page: "Work in progress" before 1.0, "Release 1.x" from 1.0.
// Switch a product over by changing its page to <StageBadge stage="release" />, only once it reaches 1.0.
const props = withDefaults(defineProps<{ stage?: 'wip' | 'release' }>(), { stage: 'wip' })
const files = { wip: 'work-in-progress', release: 'release-1x' } as const
const labels = { wip: 'Work in progress. Come build with us.', release: 'Release 1.x. Come build with us.' } as const
const file = files[props.stage]
const label = labels[props.stage]
</script>

<template>
  <p class="sw-stage">
    <a href="/stability">
      <img class="sw-light" :src="`/media/badges/${file}.svg`" :alt="label" height="56">
      <img class="sw-dark" :src="`/media/badges/${file}-on-dark.svg`" :alt="label" height="56">
    </a>
  </p>
</template>
