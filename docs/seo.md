# SEO Best Practices

This will be a lot of list items until I figure out the layout for the file:

> GitHub: 100 million "active users" in January 2023, approximately 14 million daily visitors, 96.4 million page impressions per day

| Metric            | Desktop        | Mobile |
| :---------------- | :------------- | :----- |
| SERP Title        | 50-60, (<= 70) | 50-55  |
| SERP/Meta Desc    | 120-158        | 120    |
| Explore Desc      | 143            | 143    |
| Explore Topics    | 5              | 5      |
| ~~Explore Title~~ | ~~49~~         | ~~33~~ |

- Meta description: range = 120-158, mobile = 120, 80-120 acceptable, 50-80 sometimes

> ABOUT TEXT IS USED AS GOOGLE SEO TITLE IF IT IS THE RIGHT LENGTH AND HAS THE KEYWORDS

```
README H1 character length guidance
Intro paragraph optimization
Keyword placement (early vs buried)
```

> FROM GEMINI: Google often "scrapes" the first 150–160 characters of your README to use as the meta description snippet in search results. Having a clean, keyword-rich intro with proper semantic tags like <abbr> signals to the crawler that your content is high-quality and structured
> The Pro Move: Ensure your first sentence contains your primary keyword (likely "GitHub README SEO") within the first 60 characters.

1. why are repos in Google but not in Explore?
2. why in Explore but not in Google?
3. Does the README provide enough text after the H1 for a SERP snippet?

- your repo name should use dashes ("-") separating each word and each word should be keywords that people search for, not your app name. It can be your app name if you are building an NPM package or some other tool that devs will use.
  - Dashes (-) → treated as word separators
  - Underscores (`_`) → NOT reliably treated as separators, one token or weakly split - This behavior comes from how search engines historically tokenize URLs
  - Once created, you can not edit this so get it right!
- Have a keyword rich H1 - reco char length = up to 70 characters, 50-55 ideal
- use [Capitalize My Title](https://capitalizemytitle.com/) for the correct apitalization of your H1/Title
- have a keyword rich paragraph below your H1 - reco char length =
- have keyword rich About text - reco char length --> <= 143
- Have a Table of contents if your REDME is long and/or has a lot of H2 and H3 sections
- Indent your code blocks in the Install/Getting Started section to be children elements of each ordered list item
- Have alt descriptions for all your images
- Have internal links to other files in your repo like LICENSE/LICENSE.txt, package.json, etc
- Have external links to tech stack items, resources, etc
- Use proper heading structure
- backlinks - blog/website, postings that create clicks, ...
- don't have broken links like https://localhost:8080
- have a heading structure that is common to your project type
- README word count
  - 300–800 at a minimum
  - 800–2,000 is ideal
  - 2,000–4,000 maybe, Depends on project structure/type
- make sure you star your repos - 1 is better than none

## GitHub Optimization

- Repo About text optimization
- Topics (your earlier convo—this is huge)
- Repo naming conventions
- How GitHub Explore surfaces repos
