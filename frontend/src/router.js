import { createRouter, createWebHistory } from 'vue-router';
import Auth from '@/components/Auth.vue';
import GameContainer from '@/components/GameContainer.vue';
import ProfileTest from '@/components/ProfileTest.vue';

const routes = [
  { path: '/', component: GameContainer, meta: { requiresAuth: true } },
  { path: '/auth', component: Auth },
  { path: '/test', component: ProfileTest, meta: { requiresAuth: true } }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ path: '/auth' });
  } else {
    next();
  }
});

export default router;