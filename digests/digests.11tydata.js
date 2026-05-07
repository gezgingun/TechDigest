// Applies layout + tags to every markdown file in this folder, and parses
// the date / permalink / title from the filename pattern:
//   YYYY-MM-DD_HHMM_tech-news.md
const FILENAME_RE = /^(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})/;

module.exports = {
  layout: "layouts/digest.njk",
  tags: ["digests"],
  eleventyComputed: {
    date: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return data.page.date;
      const [, y, mo, d, h, mi] = m;
      return new Date(`${y}-${mo}-${d}T${h}:${mi}:00Z`);
    },
    title: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return "Tech News Digest";
      const [, y, mo, d] = m;
      const human = new Date(`${y}-${mo}-${d}T00:00:00Z`).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
        timeZone: "UTC"
      });
      return `Tech News Digest — ${human}`;
    },
    permalink: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return false;
      const [, y, mo, d, h, mi] = m;
      return `/digests/${y}-${mo}-${d}-${h}${mi}/index.html`;
    }
  }
};
