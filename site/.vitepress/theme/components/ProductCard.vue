<script setup lang="ts">
// One product: mark, wordmark, tagline, positioning line, status, and where to go next.
import Mark from './Mark.vue'
import Word from './Word.vue'
defineProps<{ product: string; tagline: string; line: string; status: string; href: string }>()
</script>

<template>
  <a :href="href" class="sw-card">
    <span class="sw-name sw-big"><Mark :product="(product as any)" :size="34" /><Word :product="product" /></span>
    <!-- "Small. Alternative." on one line, the product's word on the next (BRAND.md, "Sites and READMEs" rule 2). -->
    <span class="sw-tag">{{ tagline.replace('Alternative. ', 'Alternative.\n') }}</span>
    <span class="sw-line">{{ line }}</span>
    <span class="sw-status">{{ status }}</span>
  </a>
</template>
