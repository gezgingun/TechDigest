const { feedPlugin } = require("@11ty/eleventy-plugin-rss");
const site = require("./_data/site.js");

// Build an absolute URL for a root-relative path (e.g. "/feed.xml").
// We use absolute URLs in HTML templates because @11ty/eleventy-plugin-rss
// has an upstream bug that registers the HtmlBasePlugin URL transform twice
// when pathPrefix is non-default — bare relative URLs would get the prefix
// applied twice. Full URLs short-circuit the transform.
function absUrl(path) {
  const p = path.startsWith("/") ? path : "/" + path;
  return site.origin + site.pathPrefix.replace(/\/$/, "") + p;
}

module.exports = function (eleventyConfig) {
  eleventyConfig.addPlugin(feedPlugin, {
    type: "atom",
    outputPath: "/feed.xml",
    collection: { name: "digests", limit: 50 },
    metadata: {
      language: "en",
      title: "Tech News Digest",
      subtitle: "Tech news rounded up from credible sources.",
      base: site.origin,
      author: { name: "Tech News Digest" }
    }
  });

  eleventyConfig.addFilter("isoDate", (d) => new Date(d).toISOString().slice(0, 10));
  eleventyConfig.addFilter("absUrl", absUrl);

  return {
    dir: { input: ".", output: "_site", includes: "_includes" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    pathPrefix: site.pathPrefix
  };
};
