import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/usuario',
    name: 'usuario',
    component: () => import('../views/UsuarioView.vue')
  },
  {
    path: '/medico',
    name: 'medico',
    component: () => import('../views/MedicoView.vue')
  },
  {
    path: '/paciente',
    name: 'paciente',
    component: () => import('../views/PacienteView.vue')
  },
  {
    path: '/auxiliar',
    name: 'auxiliar',
    component: () => import('../views/AuxiliarView.vue')
  },
  {
    path: '/familiar',
    name: 'familiar',
    component: () => import('../views/FamiliarView.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
