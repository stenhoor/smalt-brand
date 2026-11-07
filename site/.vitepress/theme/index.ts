import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
// The family theme, shared with smaltdb.dev (single copy in themes/vitepress/).
import '../../../themes/vitepress/smaltdb.css'
import './site.css'
import EngineBar from './components/EngineBar.vue'
import ProductCard from './components/ProductCard.vue'
import Mark from './components/Mark.vue'
import StageBadge from './components/StageBadge.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('EngineBar', EngineBar)
    app.component('ProductCard', ProductCard)
    app.component('Mark', Mark)
    app.component('StageBadge', StageBadge)
  },
} satisfies Theme
