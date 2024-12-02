import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "index",
    component: () => import("@/pages/LoginPage.vue"),
  },
  {
    path: "/profile/",
    name: "profile",
    component: () => import("@/pages/ProfilePage.vue"),
  },
  {
    path: "/admin/",
    name: "admin",
    component: () => import("@/pages/EmployeeDashboard.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("@/pages/NotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
