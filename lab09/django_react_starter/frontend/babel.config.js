module.exports = function (api) {
  api.cache(true);
  api.assertVersion("^7.4.5");

  const presets = [
    [
      "@babel/preset-env",
      {
        targets: {
          node: "16",
        },
      },
    ],
    "@babel/preset-react",
  ];

  const plugins = ["@babel/plugin-proposal-class-properties"];

  return {
    presets,
    plugins,
  };
};
