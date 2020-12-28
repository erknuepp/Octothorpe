import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/locations",
      name: "locations",
      component: () => import("./components/LocationsList")
    },
    {
      path: "/locations/:id",
      name: "location-details",
      component: () => import("./components/Location")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("./components/AddLocation")
    }
  ]
});