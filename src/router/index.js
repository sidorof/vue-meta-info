import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Resources from '@/views/Resources'
import Classes from '@/views/Classes'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/resources',
    name: 'Resources',
    component: Resources
  },
  {
    path: '/classes',
    name: 'Classes',
    component: Classes
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
