import { defineConfig } from 'vitepress'
import { smaltLight, smaltDark } from '../../themes/vitepress/shiki'

const GH = 'https://github.com/stenhoor'
const DESC = 'smaltworks makes the smalt family: a fast alternative database for the browser, and the tools built on it. Small data deserves good tools.'

export default defineConfig({
  title: 'smaltworks',
  description: DESC,
  lang: 'en',
  cleanUrls: true,
  // public/media holds copies of the brand files (with their READMEs); they are assets, not pages.
  srcExclude: ['public/**', 'node_modules/**', 'scripts/**'],
  lastUpdated: false,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/media/logos/smaltworks/favicon-32.svg' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@400;500&family=Martian+Mono:wght@400;600&display=swap' }],
    ['meta', { property: 'og:title', content: 'smaltworks' }],
    ['meta', { property: 'og:description', content: DESC }],
    ['meta', { property: 'og:image', content: 'https://smaltworks.dev/media/social/smaltworks.png' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ],
  markdown: { theme: { light: smaltLight, dark: smaltDark } },
  themeConfig: {
    logo: { light: '/media/logos/smaltworks/lockup.svg', dark: '/media/logos/smaltworks/lockup-on-dark.svg', alt: 'smaltworks' },
    siteTitle: false,
    nav: [
      {
        text: 'Products',
        items: [
          { text: 'Overview', link: '/products/' },
          { text: 'smaltdb · the engine', link: '/products/smaltdb' },
          { text: 'smaltql · SQL', link: '/products/smaltql' },
          { text: 'smaltdf · dataframes', link: '/products/smaltdf' },
          { text: 'smaltts · typed API', link: '/products/smaltts' },
          { text: 'smaltui · query workbench', link: '/products/smaltui' },
          { text: 'smaltbi · reports', link: '/products/smaltbi' },
          { text: 'smaltnb · notebooks', link: '/products/smaltnb' },
          { text: 'Plugins', link: '/products/plugins' },
          { text: 'Kits', link: '/products/kits' },
        ],
      },
      { text: 'Architecture', link: '/architecture' },
      { text: 'Why smalty', link: '/why-smalty' },
      { text: 'Status', link: '/status' },
      { text: 'Work in progress', link: '/stability' },
      {
        text: 'Community',
        items: [
          { text: 'Get involved', link: '/community/get-involved' },
          { text: 'Core team', link: '/community/team' },
          { text: 'Code of conduct', link: '/community/code-of-conduct' },
        ],
      },
    ],
    sidebar: [
      { text: 'smaltworks', items: [
        { text: 'Home', link: '/' },
        { text: 'Architecture', link: '/architecture' },
        { text: 'Why smalty', link: '/why-smalty' },
        { text: 'How we work with AI', link: '/ai' },
        { text: 'Status', link: '/status' },
        { text: 'Work in progress', link: '/stability' },
      ] },
      { text: 'Products', items: [
        { text: 'Overview', link: '/products/' },
        { text: 'smaltdb', link: '/products/smaltdb' },
        { text: 'smaltql', link: '/products/smaltql' },
        { text: 'smaltdf', link: '/products/smaltdf' },
        { text: 'smaltts', link: '/products/smaltts' },
        { text: 'smaltui', link: '/products/smaltui' },
        { text: 'smaltbi', link: '/products/smaltbi' },
        { text: 'smaltnb', link: '/products/smaltnb' },
        { text: 'Plugins', link: '/products/plugins' },
        { text: 'Kits', link: '/products/kits' },
      ] },
      { text: 'Community', items: [
        { text: 'Get involved', link: '/community/get-involved' },
        { text: 'Core team', link: '/community/team' },
        { text: 'Code of conduct', link: '/community/code-of-conduct' },
      ] },
      { text: 'Resources', items: [
        { text: 'Open source', link: '/open-source' },
        { text: 'Brand kit', link: '/brand' },
      ] },
    ],
    socialLinks: [{ icon: 'github', link: GH }],
    search: { provider: 'local' },
    footer: { message: 'Small. Alternative. Together. · Stay smalty.', copyright: 'MIT License' },
  },
})
