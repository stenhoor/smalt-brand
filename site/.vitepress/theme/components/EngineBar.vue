<script setup lang="ts">
// The family architecture, as the "engine bar": smaltdb is one wide bar; the sources plug in
// below it; the languages, the kits and the apps stand on it.
import Mark from './Mark.vue'
import Word from './Word.vue'
const apps = [
  { p: 'ui', what: 'SQL console', href: '/products/smaltui' },
  { p: 'bi', what: 'Reports', href: '/products/smaltbi' },
  { p: 'nb', what: 'Notebooks', href: '/products/smaltnb' },
] as const
</script>

<template>
  <figure class="sw-stack" aria-label="The smalt family architecture: sources feed one engine, smaltdb; smaltql (SQL) and smaltdf are languages on that engine; kits sit above them; smaltui, smaltbi and smaltnb are built on the kits.">
    <div class="sw-row sw-apps">
      <a v-for="a in apps" :key="a.p" :href="a.href" class="sw-box">
        <span class="sw-name"><Mark :product="a.p" :size="22" /><Word :product="a.p" /></span>
        <span class="sw-what">{{ a.what }}</span>
      </a>
    </div>
    <a href="/products/kits" class="sw-kits"><b>Kits</b> <span>small, focused libraries: fewer choices for AI agents, one consistent interface</span></a>
    <div class="sw-row sw-langs">
      <a href="/products/smaltql" class="sw-box"><span class="sw-name"><Mark product="ql" :size="22" /><Word product="ql" /></span><span class="sw-what">SQL</span></a>
      <a href="/products/smaltdf" class="sw-box"><span class="sw-name"><Mark product="df" :size="22" /><Word product="df" /></span><span class="sw-what">dataframe language</span></a>
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
