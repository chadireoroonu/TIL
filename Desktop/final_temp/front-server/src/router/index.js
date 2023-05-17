import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import LoginView from '../views/LoginView.vue'
import CommunityView from '../views/CommunityView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/MovieView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
