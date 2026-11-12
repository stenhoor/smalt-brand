<script setup lang="ts">
// The family architecture, as the "engine bar": smaltdb is one wide bar; the sources plug in
// below it; the languages, the kits (smaltty among them) and the apps stand on it.
import Mark from './Mark.vue'
import Word from './Word.vue'
const apps = [
  { p: 'ui', what: 'Query workbench', href: '/products/smaltui' },
  { p: 'bi', what: 'Reports', href: '/products/smaltbi' },
  { p: 'nb', what: 'Notebooks', href: '/products/smaltnb' },
  { p: 'fl', what: 'Pipelines', href: '/products/smaltfl' },
] as const
</script>

<template>
  <figure class="sw-stack" aria-label="The smalt family architecture: sources feed one engine, smaltdb; smaltql (SQL), smaltdf (dataframes) and smaltts (a typed API) are the ways into that engine; kits sit above them, smaltty, the TypeScript kit, among them; smaltui, smaltbi, smaltnb and smaltfl are built on the kits.">
    <div class="sw-row sw-apps">
      <a v-for="a in apps" :key="a.p" :href="a.href" class="sw-box">
        <span class="sw-name"><Mark :product="a.p" :size="22" /><Word :product="a.p" /></span>
        <span class="sw-what">{{ a.what }}</span>
      </a>
    </div>
    <div class="sw-row sw-kitrow">
      <a href="/products/smaltty" class="sw-box"><span class="sw-name"><Mark product="ty" :size="22" /><Word product="ty" /></span><span class="sw-what">TypeScript kit</span></a>
      <a href="/products/kits" class="sw-kits"><b>Kits</b> <span>small, focused libraries: fewer choices for AI agents, one consistent interface</span></a>
    </div>
    <div class="sw-row sw-langs">
      <a href="/products/smaltql" class="sw-box"><span class="sw-name"><Mark product="ql" :size="22" /><Word product="ql" /></span><span class="sw-what">SQL</span></a>
      <a href="/products/smaltdf" class="sw-box"><span class="sw-name"><Mark product="df" :size="22" /><Word product="df" /></span><span class="sw-what">dataframe language</span></a>
      <a href="/products/smaltts" class="sw-box"><span class="sw-name"><Mark product="ts" :size="22" /><Word product="ts" /></span><span class="sw-what">typed API</span></a>
    </div>
    <a href="/products/smaltdb" class="sw-engine">
      <span class="sw-name"><img src="/media/logos/smaltdb/app-icon.svg" width="40" height="40" alt="" /><span class="sw-word sw-on-smalt">sm<span class="sw-alt">alt</span>db</span></span>
      <span class="sw-engine-line">One engine. Every layer above runs on it.</span>
    </a>
    <div class="sw-row sw-sources">
      <span class="sw-src">OPFS or memory · in your browser</span>
      <span class="sw-src">External data · HTTP, S3, Azure</span>
      <span class="sw-src">Plugins · Parquet, CSV, JSON</span>
    </div>
  </figure>
</template>
