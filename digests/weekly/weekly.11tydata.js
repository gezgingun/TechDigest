// Applies to weekly rollups: digests/weekly/YYYY-MM-DD_HHMM_tech-news-weekly.md
const FILENAME_RE = /^(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})/;

module.exports = {
  layout: "layouts/digest.njk",
  tags: ["weekly"],
  pageType: "weekly",
  eleventyExcludeFromCollections: ["digests", "daily"],
  eleventyComputed: {
    date: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return data.page.date;
      const [, y, mo, d, h, mi] = m;
      return new Date(`${y}-${mo}-${d}T${h}:${mi}:00Z`);
    },
    title: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return "Weekly Digest";
      const [, y, mo, d] = m;
      const end = new Date(`${y}-${mo}-${d}T00:00:00Z`);
      const start = new Date(end);
      start.setUTCDate(start.getUTCDate() - 6);
      const fmt = (dt) => dt.toLocaleDateString("en-US", { month: "short", day: "numeric", timeZone: "UTC" });
      return `Weekly Digest — ${fmt(start)} → ${fmt(end)}, ${y}`;
    },
    permalink: (data) => {
      const m = data.page.fileSlug.match(FILENAME_RE);
      if (!m) return false;
      const [, y, mo, d, h, mi] = m;
      return `/weekly/${y}-${mo}-${d}-${h}${mi}/index.html`;
    }
  }
};
