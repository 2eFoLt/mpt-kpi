const { defineConfig } = require("@vue/cli-service");

const HOST = "0.0.0.0";
const FRONTEND_PORT = process.env.FRONTEND_PORT;
const BACKEND_PORT = process.env.BACKEND_PORT;
const BACKEND_PATH = `http://backend:${BACKEND_PORT}/`;

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    port: FRONTEND_PORT,
    host: HOST,
    proxy: {
      "/api": {
        target: BACKEND_PATH,
        secure: false,
        changeOrigin: true,
        prependPath: true,
      },
      "/media": {
        target: BACKEND_PATH,
        changeOrigin: true,
        prependPath: true,
      },
      "/static": {
        target: BACKEND_PATH,
        changeOrigin: true,
        prependPath: true,
      },
    },
  },
});
