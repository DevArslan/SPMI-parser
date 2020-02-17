import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
// import addPerson from '../views/addPerson.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/about/',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/addPerson/',
    name: 'addPerson',
    // route level code-splitting
    // this generates a separate chunk (addPerson.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "addPerson" */ '../views/addPerson.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
