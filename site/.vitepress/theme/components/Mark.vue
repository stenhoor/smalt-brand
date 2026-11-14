<script setup lang="ts">
// A product mark, light and dark, from the committed logo files.
const props = withDefaults(defineProps<{ product: 'db' | 'ui' | 'bi' | 'df' | 'nb' | 'fl' | 'ql' | 'ts' | 'cy' | 'ty' | 'works'; size?: number }>(), { size: 24 })
const FILE = { db: 'grain', ui: 'chevron', bi: 'scatter', df: 'axes', nb: 'pencil', fl: 'twin', ql: 'star', ts: 'generic', cy: 'graph', ty: 'grain', works: 'together' } as const
const base = `/media/logos/smalt${props.product}/${FILE[props.product]}-mark`
</script>

<template>
  <span class="sw-mark" :style="{ width: `${size}px`, height: `${size}px` }">
    <img class="sw-light" :src="`${base}.svg`" :width="size" :height="size" alt="" />
    <img class="sw-dark" :src="`${base}-on-dark.svg`" :width="size" :height="size" alt="" />
  </span>
</template>
