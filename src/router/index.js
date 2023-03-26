import VueRouter from "vue-router";
import TodoPage from "../page/TodoPage";


//  创建路由对象
const v = new VueRouter({
    routes: [
        {
            path: "/",
            component: TodoPage
        }
    ]
})
export default v;
