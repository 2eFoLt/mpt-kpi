import { createMemoryHistory, createRouter } from "vue-router";

import Main from "@/pages/Main.vue";
import NotFound from "@/pages/NotFound.vue";

const routes_list = [
  { path: "/", name: "Main", component: Main },
  { path: "/:pathMatch(.*)*", name: "Not Found", component: NotFound },
];

const router = createRouter({
  history: createMemoryHistory(),
  routes: routes_list,
});

export default router;
